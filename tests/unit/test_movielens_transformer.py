from app.data.loaders.movielens_loader import MovieLensLoader 
from app.data.transformers.movielens_transformer import MovieLensTransformer 

loader = MovieLensLoader()
movies = loader.load_movies()
transformer = MovieLensTransformer()

movies_clean = transformer.transform(movies)

print(movies_clean.head())
print(movies_clean.columns)