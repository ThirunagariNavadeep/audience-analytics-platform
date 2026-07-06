import pandas as pd
from app.repository.feature_repository import FeatureRepository
from app.feature_engineering.synthetic_feature_builder import SyntheticFeatureBuilder
from app.recommender.similarity import SimilarityEngine
from app.recommender.content_based import ContentBasedRecommender

repo = FeatureRepository()

movies = repo.load_analytics_movies()

builder = SyntheticFeatureBuilder()

features = builder.build(movies)

engine = SimilarityEngine()

scaled = engine.fit(
    features,
    [
        "average_rating",
        "rating_count",
        "movie_age",
        "genre_count",
        "rating_confidence"
    ]
)

recommender = ContentBasedRecommender(
    engine
)

recommendations = recommender.recommend_by_title(
    features,
    scaled,
    "Toy Story",
    k=5
)

pd.set_option("display.max.columns", None)
pd.set_option("display.max.colwidth", None)
pd.set_option("display.width", 200)

print(recommendations)