import pandas as pd 
from app.core.logging import logger

class PopularityFeatures:
    def build(
        self,
        dataframe: pd.DataFrame
    ) -> pd.DataFrame:

        logger.info("Generating Popularity Features")

        df = dataframe.copy()

        median_rating_count = (
            df["rating_count"].median()
        )

        df["popular_movie"] = (
            df["rating_count"] >= median_rating_count
        )

        df["highly_rated"] = (
            df["average_rating"] >= 4.0
        )

        df["rating_bucket"] = pd.cut(
            df["average_rating"],
            bins = [0, 2, 3, 4, 5],
            labels = ["Poor", "Average", "Good", "Excellent"],
            include_lowest = True
        )

        df["rating_confidence"] = (
            df["rating_count"] * df["average_rating"]
        )

        logger.info("Popularity Features Generated")

        return df