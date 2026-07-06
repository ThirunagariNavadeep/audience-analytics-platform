from app.repository.feature_repository import FeatureRepository

repo = FeatureRepository()

movies = repo.load_analytics_movies()

print("Dataset Shape:")
print(movies.shape)

print("\nMissing Values:")
print(
    movies[
        [
            "rating_count",
            "average_rating",
            "rating_min",
            "rating_max",
            "unique_users",
            "active_days",
            "release_year"
        ]
    ].isna().sum()
)

print("\nFirst 5 Rows:")
print(
    movies[
        [
            "movie_id",
            "title",
            "rating_count",
            "average_rating",
            "release_year"
        ]
    ].head()
)