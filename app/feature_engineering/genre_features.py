
import pandas as pd

from app.core.logging import logger


class GenreFeatures:
    def build(
        self,
        dataframe: pd.DataFrame
    ) -> pd.DataFrame:

        logger.info(
            "Generating Genre Features"
        )

        df = dataframe.copy()

        df["genre_count"] = df["genres_list"].apply(
            lambda genres: len(genres)
            if genres is not None
            else 0
        )

        df["primary_genre"] = df["genres_list"].apply(
            lambda genres: (
                genres[0]
                if genres is not None and len(genres) > 0
                else "Unknown"
            )
        )

        df["multi_genre_movie"] = (
            df["genre_count"] > 1
        )

        df["genre_diversity"] = df["genre_count"].apply(
            self.get_genre_diversity
        )

        logger.info(
            "Genre Features Generated"
        )

        return df

    @staticmethod
    def get_genre_diversity(
        count: int
    ) -> str:
        
        if count <= 1:
            return "Low"

        elif count <= 3:
            return "Medium"

        else:
            return "High"