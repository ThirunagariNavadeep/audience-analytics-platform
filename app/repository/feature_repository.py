from pathlib import Path 
import pandas as pd 
from app.core.logging import logger

class FeatureRepository:
   
    def __init__(
        self,
        feature_dir: Path = Path("data/features"),
        processed_dir: Path = Path("data/processed"),
        analytics_dir: Path = Path("data/analytics")
    ):

        self.feature_dir = feature_dir
        self.processed_dir = processed_dir
        self.analytics_dir = analytics_dir

    def _load_parquet(
        self,
        file_path: Path 
    ) -> pd.DataFrame:
        """
        Load a parquet dataset.
        """

        if not file_path.exists():
            raise FileNotFoundError(
                f"Dataset not found: {file_path}"
            )

        logger.info(
            f"Loading dataset: {file_path.name}"
        )

        return pd.read_parquet(file_path)

    def load_user_features(
        self
    ) -> pd.DataFrame:
        """
        Load a parquet dataset.
        """
        return self._load_parquet(
            self.feature_dir / "user_features.parquet"
        )

    def load_movie_features(
        self
    ) -> pd.DataFrame:
        """
        Load movie feature dataset.
        """
        return self._load_parquet(
            self.feature_dir / "movie_features.parquet"
        )

    def load_processed_movies(
        self
    ) -> pd.DataFrame:
        """
        Load processed movie metadata.
        """
        return self._load_parquet(
            self.processed_dir / "movies_clean.parquet"
        )

    def load_analytics_movies(
        self
    ) -> pd.DataFrame:
        """
        Load the analytics movie dataset:
        """

        return self._load_parquet(
            Path("data/analytics/analytics_movies.parquet")
        )

    def load_processed_links(
        self
    ) -> pd.DataFrame:
        """
        Load processed MovieLens links dataset.
        """

        return self._load_parquet(self.processed_dir / "links_clean.parquet")


    def save_parquet(
        self,
        dataframe: pd.DataFrame,
        filename: str 
    ) -> None:

        self.feature_dir.mkdir(
            parents = True,
            exist_ok = True
        )

        output_path = self.feature_dir / filename

        logger.info(f"Saving dataset: {output_path.name}")

        dataframe.to_parquet(
            output_path,
            index = False
        )

    def save_csv(
        self,
        dataframe: pd.DataFrame,
        filename: str 
    ) -> None:

        self.feature_dir.mkdir(
            parents = True,
            exist_ok = True
        )

        output_path = self.feature_dir / filename

        logger.info(f"Saving dataset: {output_path.name}")

        dataframe.to_csv(output_path, index = False)

