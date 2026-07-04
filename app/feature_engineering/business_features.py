from datetime import datetime
import numpy as np 
import pandas as pd 
from app.core.logging import logger 

class BusinessFeatures:
    def build(
        self,
        dataframe: pd.DataFrame
    ) -> pd.DataFrame:

        logger.info("Generating Business Features")

        df = dataframe.copy()

        current_year = datetime.now().year 

        df["movie_age"] = (
            current_year - df["release_year"]
        )

        if ("revenue" in df.columns and "runtime" in df.columns):

            df["revenue_per_minute"] = (
                df["revenue"] / df["runtime"]
            ).replace([np.inf, -np.inf], np.nan)

        if ("revenue" in df.columns and "budget" in df.columns):

            df["profit"] = (df["revenue"] - df["budget"])

        if ("revenue" in df.columns and "budget" in df.columns):
            dataframe["budget_efficiency"] = (df["revenue"] / df["budget"]).replace(
                [np.inf, -np.inf], np.nan
            )

        if ("profit" in df.columns and "budget" in df.columns):
            dataframe["profit_margin"] = (df[profit] / df["budget"]).replace(
                [np.inf, -np.inf], np.nan
            )

        logger.info("Business Features Generated")

        return df

