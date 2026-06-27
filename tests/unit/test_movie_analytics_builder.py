from pathlib import Path 
from app.repository.feature_repository import FeatureRepository
from app.analytics.movie_analytics_builder import MovieAnalyticsBuilder
from app.features.feature_writer import FeatureWriter

repo = FeatureRepository()

movies = repo.load_processed_movies()

movies_features = repo.load_movie_features()

builder = MovieAnalyticsBuilder()

analytics = builder.build(
    movies,
    movies_features
)

writer = FeatureWriter(
    Path("data/analytics")
)

writer.save_parquet(
    analytics,
    "analytics_movies.parquet"
)

writer.save_csv(
    analytics,
    "analytics_movie.csv"
)

print(analytics.head())
print(analytics.shape)
