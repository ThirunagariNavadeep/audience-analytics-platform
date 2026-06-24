"""
User Feature Builder

Builds user-level behavioral features
from MovieLens ratings data.
"""

import pandas as pd 
from app.core.logging import logger

class UserFeatureBuilder:
    def build(
        self,
        ratings_df: pd.DataFrame
    ) -> pd.DataFrame:

        logger.info("Building User Features")
        ratings_df = ratings_df.copy()

        ratings_df["timestamp"] = pd.to_datetime(
            ratings_df["timestamp"],
            unit = "s"
        )

        user_features = (
            ratings_df
            .groupby("userId")
            .agg(
                total_ratings = (
                    "rating",
                    "count"
                ),
                avg_ratings = (
                    "rating",
                    "mean"
                ),
                min_rating = (
                    "rating",
                    "min"
                ),
                max_ratings = (
                    "rating",
                    "max"
                ),
                rating_std = (
                    "rating",
                    "std"
                ),
                movies_watched = (
                    "movieId",
                    "nunique"
                ),
                first_rating_date = (
                    "timestamp",
                    "min"
                ),
                last_rating_date = (
                    "timestamp",
                    "max"
                )
            )
            .reset_index()
        )

        user_features["active_days"] = (
            user_features["last_rating_date"] - user_features["first_rating_date"]
        ).dt.days 

        logger.info("User Feature Generation Complete")

        return user_features