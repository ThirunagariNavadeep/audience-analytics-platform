"""
Analytics Dataset Validator

Performs quality checks on the analytics dataset.
"""

import pandas as pd

from app.core.logging import logger


class AnalyticsValidator:
    """
    Validates the analytics movie dataset.
    """

    def validate(
        self,
        dataframe: pd.DataFrame
    ) -> dict:
        """
        Validate the analytics dataset.
        """

        logger.info("Validating analytics dataset")

        report = {
            "valid": True,
            "total_rows": int(len(dataframe)),
            "errors": {},
            "warnings": {}
        }

     
        report["errors"]["duplicate_movie_ids"] = (
            self._duplicate_movie_ids(dataframe)
        )

        report["errors"]["invalid_average_ratings"] = (
            self._invalid_average_ratings(dataframe)
        )

        report["errors"]["negative_rating_counts"] = (
            self._negative_rating_counts(dataframe)
        )

        report["warnings"]["missing_titles"] = (
            self._missing_titles(dataframe)
        )

        report["warnings"]["missing_release_years"] = (
            self._missing_release_years(dataframe)
        )

    
        report["valid"] = all(
            value == 0
            for value in report["errors"].values()
        )

        logger.info("Analytics validation complete")

        return report


    def _duplicate_movie_ids(
        self,
        dataframe: pd.DataFrame
    ) -> int:

        return int(
            dataframe["movie_id"]
            .duplicated()
            .sum()
        )

    def _invalid_average_ratings(
        self,
        dataframe: pd.DataFrame
    ) -> int:

        return int(
            dataframe[
                (dataframe["average_rating"] < 0)
                |
                (dataframe["average_rating"] > 5)
            ].shape[0]
        )

    def _negative_rating_counts(
        self,
        dataframe: pd.DataFrame
    ) -> int:

        return int(
            dataframe[
                dataframe["rating_count"] < 0
            ].shape[0]
        )


    def _missing_titles(
        self,
        dataframe: pd.DataFrame
    ) -> int:

        return int(
            dataframe["title"]
            .isna()
            .sum()
        )

    def _missing_release_years(
        self,
        dataframe: pd.DataFrame
    ) -> int:

        return int(
            dataframe["release_year"]
            .isna()
            .sum()
        )