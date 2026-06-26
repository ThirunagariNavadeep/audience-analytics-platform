"""
Streaming User Feature Builder

Builds user-level statistics incrementally
from MovieLens ratings data.
"""

import pandas as pd

from app.core.logging import logger
from app.features.models import UserStatistics


class UserFeatureBuilder:
    """
    Streaming feature engineering for user-level statistics.
    """

    def __init__(self):
        """
        Initialize the global user statistics dictionary.
        """

        self.user_statistics: dict[int, UserStatistics] = {}

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

        chunk = chunk.copy()

        chunk["timestamp"] = pd.to_datetime(
            chunk["timestamp"],
            unit="s"
        )

        chunk_summary = (
            chunk
            .groupby("userId")
            .agg(
                rating_count=("rating", "count"),
                rating_sum=("rating", "sum"),
                rating_min=("rating", "min"),
                rating_max=("rating", "max"),
                movies_seen=(
                    "movieId",
                    lambda x: set(x)
                ),
                first_timestamp=(
                    "timestamp",
                    "min"
                ),
                last_timestamp=(
                    "timestamp",
                    "max"
                )
            )
            .reset_index()
        )

      
        chunk_summary = chunk_summary.rename(
            columns={
                "userId": "user_id"
            }
        )

        logger.info(
            f"Chunk summarized into {len(chunk_summary):,} users"
        )

        self._merge_chunk_statistics(chunk_summary)

    def _merge_chunk_statistics(
        self,
        chunk_summary: pd.DataFrame
    ) -> None:
        """
        Merge summarized statistics into
        the global user statistics.
        """

        logger.info(
            "Merging chunk statistics"
        )

        for row in chunk_summary.itertuples(index=False):

            user_id = row.user_id

            if user_id not in self.user_statistics:
                self.user_statistics[user_id] = UserStatistics()

            stats = self.user_statistics[user_id]

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

            stats.movies_seen |= row.movies_seen

            if (
                stats.first_timestamp is None
                or row.first_timestamp < stats.first_timestamp
            ):
                stats.first_timestamp = row.first_timestamp

            if (
                stats.last_timestamp is None
                or row.last_timestamp > stats.last_timestamp
            ):
                stats.last_timestamp = row.last_timestamp

        logger.info(
            f"Global users tracked: {len(self.user_statistics):,}"
        )

    def finalize(
        self
    ) -> pd.DataFrame:
        """
        Convert accumulated statistics into
        a user feature DataFrame.
        """

        logger.info(
            "Building final user feature dataset"
        )

        records = []

        for user_id, stats in self.user_statistics.items():

            active_days = 0

            if (
                stats.first_timestamp is not None
                and stats.last_timestamp is not None
            ):
                active_days = (
                    stats.last_timestamp
                    - stats.first_timestamp
                ).days

            records.append(
                {
                    "user_id": user_id,
                    "rating_count": stats.rating_count,
                    "average_rating": round(
                        stats.average_rating(),
                        2
                    ),
                    "rating_min": stats.rating_min,
                    "rating_max": stats.rating_max,
                    "movies_watched": stats.movies_watched(),
                    "active_days": active_days,
                    "first_rating": stats.first_timestamp,
                    "last_rating": stats.last_timestamp
                }
            )

        user_features = pd.DataFrame(records)

        logger.info(
            f"Created User Feature Dataset with {len(user_features):,} users"
        )

        return user_features

        print(total_chunks)