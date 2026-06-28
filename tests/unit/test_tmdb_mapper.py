from app.enrichment.tmdb_client import TMDBClient
from app.enrichment.tmdb_mapper import TMDBMapper

client = TMDBClient()

mapper = TMDBMapper()

movie_json = client.get_movie(862)

movie = mapper.map_movie(
    movie_json
)

print(movie)

movie_json = client.get_movie(862)

print(movie_json.keys())

print(movie_json["production_companies"])