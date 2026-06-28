from app.repository.feature_repository import FeatureRepository

repo = FeatureRepository()

users = repo.load_user_features()

movies = repo.load_movie_features()

processed_movies = repo.load_processed_movies()

links = repo.load_processed_links()

print(users.shape)

print(movies.shape)

print(processed_movies.shape)

print(links.head())

print(links.shape)