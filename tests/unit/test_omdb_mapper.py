from app.enrichment.omdb_client import OMDBClient
from app.enrichment.omdb_mapper import OMDbMapper

client = OMDBClient()

mapper = OMDbMapper()

movie_json = client.get_movie(
    "tt0114709"
)

movie = mapper.map_movie(
    movie_json
)

print(movie)