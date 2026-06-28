from app.enrichment.tmdb_client import TMDBClient

client = TMDBClient()

movie = client.get_movie(862)

print("=" * 50)
print(movie["title"])
print(movie["release_date"])
print(movie["runtime"])
print(movie["vote_average"])
print(movie["genres"])
print("=" * 50)