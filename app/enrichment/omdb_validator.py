"""
OMDb Dataset Validator

Validates the enriched OMDb dataset.
"""

import pandas as pd 
from app.core.logging import logger

class OMDbValidator:
    def validate(
        self,
        dataframe: pd.DataFrame
    ) -> dict:

        logger.info("Validating OMDb dataset")

        errors = {
            "duplicate_movie_ids": int(
                dataframe["movie_id"].duplicated().sum()
            ),

            "missing_imdb_ids": int(
                dataframe["imdb_id"].isna().sum()
            ),

            "invalid_imdb_rating": int((
                (dataframe["imdb_rating"] < 0) | (dataframe["imdb_rating"] > 10)
            ).sum()),

            "invalid_metascore": int((
                (dataframe["metascore"] < 0) | (dataframe["metascore"] > 100)
            ).sum()),
        }

        warnings = {

            "missing_runtime": int(
                dataframe["runtime_omdb"].isna().sum()
            ),

            "missing_plot": int(
                dataframe["plot"].isna().sum()
            ),

            "missing_director": int(
                dataframe["director"].apply(
                    lambda x: len(x) == 0 if isinstance(x, list) else True
                ).sum()
            ),

            "missing_writer": int(
                dataframe["writer"].apply(
                    lambda x: len(x) == 0 if isinstance(x, list) else True).sum()
            ),

            "missing_actors": int(
                dataframe["actors"].apply(
                    lambda x: len(x) == 0 if isinstance(x, list) else True
                ).sum()
            ),

            "missing_genre": int(
                dataframe["genre_omdb"].apply(
                    lambda x: len(x) == 0 if isinstance(x, list) else True
                ).sum()
            ),

            "missing_country": int(
                dataframe["country"].apply(
                    lambda x: len(x) == 0 if isinstance(x, list) else True
                ).sum()
            ),

            "missing_language": int(
                dataframe["language"].apply(
                    lambda x: len(x) == 0 if isinstance(x, list) else True
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

        logger.info("OMDb Validation complete")

        return report