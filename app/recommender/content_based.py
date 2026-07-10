import pandas as pd

from app.core.logging import logger
from app.recommender.similarity import SimilarityEngine


class ContentBasedRecommender:

    def __init__(
        self,
        similarity_engine: SimilarityEngine
    ):

        self.engine = similarity_engine

    def recommend_by_index(
        self,
        dataframe: pd.DataFrame,
        scaled_features,
        movie_index: int,
        k: int = 10
    ) -> pd.DataFrame:

        logger.info(
            "Generating movie recommendations"
        )

        distances, indices = self.engine.nearest_movies(
            scaled_features,
            movie_index,
            k
        )

        recommendations = dataframe.iloc[
            indices
        ].copy()

        recommendations["similarity_score"] = (
            1 - distances
        )

        recommendations = recommendations[
            [
                "movie_id",
                "title",
                "genres",
                "average_rating",
                "rating_count",
                "similarity_score"
            ]
        ]

        recommendations = recommendations.sort_values(
            by="similarity_score",
            ascending=False
        )

        return recommendations.reset_index(
            drop=True
        )

    def recommend_by_title(
        self,
        dataframe: pd.DataFrame,
        scaled_features,
        title: str,
        k: int = 10
    ) -> pd.DataFrame:

        logger.info(
            f"Searching for movie: {title}"
        )

        matches = dataframe[
            dataframe["title"].str.contains(
                title,
                case=False,
                na=False
            )
        ]

        if matches.empty:

            raise ValueError(
                f"Movie '{title}' not found."
            )

        movie_index = matches.index[0]

        logger.info(
            f"Matched movie: {matches.iloc[0]['title']}"
        )

        return self.recommend_by_index(
            dataframe,
            scaled_features,
            movie_index,
            k
        )
