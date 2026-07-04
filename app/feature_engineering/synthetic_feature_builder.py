import pandas as pd
from app.core.logging import logger
from app.feature_engineering.business_features import BusinessFeatures
from app.feature_engineering.temporal_features import TemporalFeatures
from app.feature_engineering.popularity_features import PopularityFeatures
from app.feature_engineering.genre_features import GenreFeatures

class SyntheticFeatureBuilder:
    def __init__(self) -> None:
        self.business = BusinessFeatures()
        self.temporal = TemporalFeatures()
        self.popularity = PopularityFeatures()
        self.genre = GenreFeatures()
        logger.info("Initializing Synthetic Feature Builder")


    def build(
        self,
        dataframe: pd.DataFrame
    ) -> pd.DataFrame:

        logger.info("Starting synthetic feature engineering")

        df = dataframe.copy()

        df = self.business.build(df)

        df = self.temporal.build(df)

        df = self.popularity.build(df)

        df = self.genre.build(df)

        logger.info(f"Created dataset with {df.shape[1]} columns")

        return df

