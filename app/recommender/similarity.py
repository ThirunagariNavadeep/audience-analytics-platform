import pandas as pd

from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler

from app.core.logging import logger


class SimilarityEngine:

    def __init__(self):

        self.scaler = StandardScaler()

        self.model = NearestNeighbors(
            metric = "cosine",
            algorithm = "brute"
        )

    def fit(
        self,
        dataframe: pd.DataFrame,
        columns: list[str]
    ):

        logger.info("Training Similarity Model")

        features = dataframe[columns].copy()

        features = features.fillna(0)

        scaled = self.scaler.fit_transform(features)

        self.model.fit(scaled)

        logger.info("Similarity Model Ready")

        return scaled


    def nearest_movies(
        self,
        scaled_features,
        movie_index: int, k: int = 10
    ):

        distances, indices = self.model.kneighbors(
            scaled_features[movie_index].reshape(1, -1),
            n_neighbors = k + 1
        )

        return distances[0][1:], indices[0][1:]    