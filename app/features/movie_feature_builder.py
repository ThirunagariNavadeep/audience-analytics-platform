"""
Streaming Movie Feature Builder

Builds movie-level statistics incrementally
from MovieLens ratings data.
"""

import pandas as pd

from app.core.logging import logger
from app.features.movie_models import MovieStatistics


class MovieFeatureBuilder:
    """
    Streaming feature engineering for movie-level statistics.
    """

    def __init__(self):
        """
        Initialize the global movie statistics dictionary.
        """

        self.movie_statistics: dict[int, MovieStatistics] = {}

    def process_chunk(
        self,
        chunk: pd.DataFrame
    ) -> None:
        """
        Process one chunk of ratings data.
        """

        logger.info(
            f"Processing chunk with {len(chunk):,} rows"
        )

        # Work on a copy
        chunk = chunk.copy()

        # Convert Unix timestamp to datetime
        chunk["timestamp"] = pd.to_datetime(
            chunk["timestamp"],
            unit="s"
        )

        # Summarize this chunk
        chunk_summary = (
            chunk
            .groupby("movieId")
            .agg(
                rating_count=("rating", "count"),
                rating_sum=("rating", "sum"),
                rating_min=("rating", "min"),
                rating_max=("rating", "max"),
                unique_users=(
                    "userId",
                    lambda x: set(x)
                ),
                first_rating=(
                    "timestamp",
                    "min"
                ),
                last_rating=(
                    "timestamp",
                    "max"
                )
            )
            .reset_index()
        )

        # Standardize column names
        chunk_summary = chunk_summary.rename(
            columns={
                "movieId": "movie_id"
            }
        )

        logger.info(
            f"Chunk summarized into {len(chunk_summary):,} movies"
        )

        self._merge_chunk_statistics(chunk_summary)

    def _merge_chunk_statistics(
        self,
        chunk_summary: pd.DataFrame
    ) -> None:
        """
        Merge summarized statistics into
        the global movie statistics.
        """

        logger.info(
            "Merging chunk statistics"
        )

        for row in chunk_summary.itertuples(index=False):

            movie_id = row.movie_id

            if movie_id not in self.movie_statistics:
                self.movie_statistics[movie_id] = MovieStatistics()

            stats = self.movie_statistics[movie_id]

            stats.rating_count += row.rating_count

            stats.rating_sum += row.rating_sum

            stats.rating_min = min(
                stats.rating_min,
                row.rating_min
            )

            stats.rating_max = max(
                stats.rating_max,
                row.rating_max
            )

            stats.unique_users |= row.unique_users

            if (
                stats.first_rating is None
                or row.first_rating < stats.first_rating
            ):
                stats.first_rating = row.first_rating

            if (
                stats.last_rating is None
                or row.last_rating > stats.last_rating
            ):
                stats.last_rating = row.last_rating

        logger.info(
            f"Global movies tracked: {len(self.movie_statistics):,}"
        )

    def finalize(
        self
    ) -> pd.DataFrame:
        """
        Convert accumulated statistics into
        a movie feature DataFrame.
        """

        logger.info(
            "Building final movie feature dataset"
        )

        records = []

        for movie_id, stats in self.movie_statistics.items():

            active_days = 0

            if (
                stats.first_rating is not None
                and stats.last_rating is not None
            ):
                active_days = (
                    stats.last_rating
                    - stats.first_rating
                ).days

            records.append(
                {
                    "movie_id": movie_id,

                    "rating_count": stats.rating_count,

                    "average_rating": round(
                        stats.average_rating(),
                        2
                    ),

                    "rating_min": stats.rating_min,

                    "rating_max": stats.rating_max,

                    "unique_users": stats.total_users(),

                    "active_days": active_days,

                    "first_rating": stats.first_rating,

                    "last_rating": stats.last_rating
                }
            )

        movie_features = pd.DataFrame(records)

        logger.info(
            f"Created Movie Feature Dataset with {len(movie_features):,} movies"
        )

        return movie_features