from app.repository.feature_repository import FeatureRepository

repo = FeatureRepository()

users = repo.load_user_features()

movies = repo.load_movie_features()

processed_movies = repo.load_processed_movies()

print(users.shape)

print(movies.shape)

print(processed_movies.shape)