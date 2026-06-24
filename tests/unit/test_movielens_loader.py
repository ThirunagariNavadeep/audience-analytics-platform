from app.data.loaders.movielens_loader import MovieLensLoader

loader = MovieLensLoader()

movies = loader.load_movies()

print("\n Movies Dataset")
print("-"*50)
print(movies.head())
print(f"\nShape: {movies.shape}")
print(movies.info())

