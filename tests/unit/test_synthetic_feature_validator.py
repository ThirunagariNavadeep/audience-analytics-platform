from datetime import datetime
from app.repository.feature_repository import FeatureRepository 
from app.feature_engineering.synthetic_feature_builder import SyntheticFeatureBuilder
from app.validation.synthetic_feature_validator import SyntheticFeatureValidator

repo = FeatureRepository()

movies = repo.load_analytics_movies()

builder = SyntheticFeatureBuilder()

features = builder.build(movies)

validator = SyntheticFeatureValidator()

report = validator.validate(features)

print(report)

