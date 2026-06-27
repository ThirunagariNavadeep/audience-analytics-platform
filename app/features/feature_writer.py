"""
Feature Writer

Persists engineered features to disk.
"""

from pathlib import Path

import pandas as pd

from app.core.logging import logger


class FeatureWriter:
    """
    Saves feature datasets.
    """

    def __init__(
        self,
        output_dir: Path
    ):

        self.output_dir = output_dir

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

    def save_parquet(
        self,
        dataframe: pd.DataFrame,
        filename: str
    ) -> Path:
        """
        Save a DataFrame as a Parquet file.
        """

        output_path = self.output_dir / filename

        dataframe.to_parquet(
            output_path,
            index=False
        )

        logger.info(
            f"Saved feature dataset: {output_path}"
        )

        return output_path

    def save_csv(
        self,
        dataframe: pd.DataFrame,
        filename: str
    ) -> Path:
        """
        Save a DataFrame as CSV.
        """

        output_path = self.output_dir / filename

        dataframe.to_csv(
            output_path,
            index=False
        )

        logger.info(
            f"Saved feature dataset: {output_path}"
        )

        return output_path

       

