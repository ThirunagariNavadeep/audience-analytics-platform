import pandas as pd 
from app.core.logging import logger

class MovieAnalyticsBuilder:
    def build (
        self,
        movies: pd.DataFrame,
        movie_features: pd.DataFrame
    ) -> pd.DataFrame:

        logger.info("Building analytics movie dataset")

        analytics = movies.merge(
            movie_features,
            on = "movie_id",
            how = "left"
        )

        logger.info(
            f"Analytical dataset contains {len(analytics):,} movies"
        )

        return analytics
