from app.data.loaders.movielens_loader import(MovieLensLoader)
from app.data.validators.movielens_validator import(MovieLensValidator)

loader = MovieLensLoader()
movies = loader.load_movies()
validator = MovieLensValidator()
results = validator.validate_movies(movies)

print(results)