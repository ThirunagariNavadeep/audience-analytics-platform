from pathlib import Path 
from app.data.loaders.ratings_loader import RatingsLoader
from app.features.user_feature_builder import UserFeatureBuilder

loader = RatingsLoader(
    Path(
        "data/raw/movielens/ratings.csv"
    )
)

ratings = loader.load_sample(100000)

builder = UserFeatureBuilder()

features = builder.build(ratings)

print(features.head())

print(features.shape)