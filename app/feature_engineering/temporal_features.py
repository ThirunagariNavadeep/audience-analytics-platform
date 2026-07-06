from datetime import datetime
import pandas as pd 
from app.core.logging import logger

class TemporalFeatures:
    def build(
        self,
        dataframe: pd.DataFrame
    ) -> pd.DataFrame:

        logger.info("Generating Temporal Features")

        df = dataframe.copy()

        current_year = datetime.now().year 

        if "movie_age" not in df.columns:
            df["movie_age"] = (current_year - df["release_year"]).fillna(-1)

        df["release_decade"] = ((df["release_year"] // 10) * 10)

        df["classic_movie"] = (df["movie_age"] >= 25)

        df["modern_movie"] = ((df["movie_age"] >= 10) & (df["movie_age"] < 25))

        df["recent_movie"] = (df["movie_age"] < 10)

        logger.info("Temporal Features Generated")

        return df