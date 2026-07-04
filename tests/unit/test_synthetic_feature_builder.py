from app.repository.feature_repository import FeatureRepository 
from app.feature_engineering.synthetic_feature_builder import SyntheticFeatureBuilder

repo = FeatureRepository()

movies = repo.load_analytics_movies()

builder = SyntheticFeatureBuilder()

features = builder.build(movies)

print(features.head())

print()

print(features.shape)

print()

print(features.columns.tolist())