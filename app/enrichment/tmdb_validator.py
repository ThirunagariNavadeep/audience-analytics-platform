"""
TMDB Dataset Validator

Validates the enriched TMDB movie dataset.
"""

import pandas as pd 
from app.core.logging import logger

class TMDBValidator:
    """
    Validate the enriched TMDB dataset.
    """

    def validate(
        self,
        dataframe: pd.DataFrame
    ) -> dict:

        logger.info("Validating TMDB dataset")

        errors = {
            "duplicate_movie_ids": int(
                dataframe["tmdb_id"].duplicated().sum()
            ),

            "missing_tmdb_ids": int(
                dataframe["tmdb_id"].isna().sum()
            ),

            "invalid_vote_average": int(
                (
                    (dataframe["vote_average_tmdb"] < 0) | (dataframe["vote_average_tmdb"] > 10)
                ).sum()
            )
        }

        warnings = {
            "missing_runtime": int(
                dataframe["runtime"].isna().sum()
            ),

            "missing_budget": int(
                dataframe["budget"].isna().sum()
            ),

            "missing_revenue": int(
                dataframe["revenue"].isna().sum()
            ),

            "missing_homepage": int(
                dataframe["homepage"].isna().sum()
            ),

            "missing_collection": int(
                dataframe["collection"].isna().sum()
            ),

            "missing_original_language": int(
                dataframe["original_language"].isna().sum()
            ),

            "empty_genres": int(
                dataframe["tmdb_genres"].apply(
                    lambda x: len(x) == 0
                ).sum()
            ),

            "empty_production_companies": int(
                dataframe["production_companies"].apply(
                    lambda x: len(x) == 0
                ).sum()            
            ) 
        }

        valid = all(
            value == 0
            for value in errors.values()
        )

        report = {
            "valid": valid,
            "total_rows": len(dataframe),
            "errors": errors,
            "warnings": warnings
        }

        logger.info("TMDB validation complete")

        return report