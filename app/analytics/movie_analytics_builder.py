"""
Movie Analytics Builder

Builds the analytics-ready movie dataset by
combining movie metadata with aggregated
movie rating features.
"""

import pandas as pd

from app.core.logging import logger


class MovieAnalyticsBuilder:
    """
    Build the analytics movie dataset.
    """

    def build(
        self,
        movies: pd.DataFrame,
        movie_features: pd.DataFrame
    ) -> pd.DataFrame:

        logger.info(
            "Building analytics movie dataset"
        )

        #
        # Merge movie metadata with
        # aggregated movie statistics
        #

        analytics = movies.merge(
            movie_features,
            on="movie_id",
            how="left"
        )

       #
        # Fill missing values for movies
        # that have never been rated.
        #

        numeric_defaults = {

            "rating_count": 0,

            "average_rating": 0.0,

            "rating_min": 0.0,

            "rating_max": 0.0,

            "unique_users": 0,

            "active_days": 0

        }

        for column, default_value in numeric_defaults.items():

            if column in analytics.columns:

                analytics[column] = analytics[column].fillna(
                    default_value
                )

        #
        # Ensure datetime columns are
        # valid timestamps.
        #

        datetime_columns = [

            "first_rating",

            "last_rating"

        ]

        for column in datetime_columns:

            if column in analytics.columns:

                analytics[column] = pd.to_datetime(
                    analytics[column],
                    errors="coerce"
                )

        logger.info(
            f"Analytics dataset contains {len(analytics):,} movies"
        )

        return analytics