from datetime import datetime

import pandas as pd

from app.core.logging import logger


class SyntheticFeatureValidator:
  
    def validate(
        self,
        dataframe: pd.DataFrame
    ) -> dict:

        logger.info(
            "Validating Synthetic Features"
        )

        current_year = datetime.now().year
        min_release_decade = 1870

        errors = {

            "negative_movie_age": int(
                (
                    dataframe["movie_age"] < 0
                ).sum()
            ),

            "invalid_release_decade": int(
                (
                    (dataframe["release_decade"] < min_release_decade)
                    |
                    (dataframe["release_decade"] > current_year)
                ).sum()
            ),

            "invalid_rating_bucket": int(
                (
                    dataframe["rating_bucket"].notna()
                    &
                    ~dataframe["rating_bucket"].isin(
                        [
                            "Poor",
                            "Average",
                            "Good",
                            "Excellent"
                        ]
                    )
                ).sum()
            ),

            "negative_rating_confidence": int(
                (
                    dataframe["rating_confidence"] < 0
                ).sum()
            ),

            "negative_genre_count": int(
                (
                    dataframe["genre_count"] < 0
                ).sum()
            ),

            "missing_primary_genre": int(
                (
                    dataframe["primary_genre"] == "Unknown"
                ).sum()
            ),

            "invalid_genre_diversity": int(
                (
                    dataframe["genre_diversity"].notna()
                    &
                    ~dataframe["genre_diversity"].isin(
                        [
                            "Low",
                            "Medium",
                            "High"
                        ]
                    )
                ).sum()
            )

        }

        warnings = {

            "classic_movies": int(
                dataframe["classic_movie"].sum()
            ),

            "recent_movies": int(
                dataframe["recent_movie"].sum()
            ),

            "popular_movies": int(
                dataframe["popular_movie"].sum()
            ),

            "highly_rated_movies": int(
                dataframe["highly_rated"].sum()
            ),

            "missing_rating_bucket": int(
                dataframe["rating_bucket"].isna().sum()
            )

        }

        report = {

            "valid": all(
                value == 0
                for value in errors.values()
            ),

            "total_rows": len(dataframe),

            "errors": errors,

            "warnings": warnings

        }

        logger.info(
            "Synthetic Feature Validation Complete"
        )

        return report

       