from app.enrichment.omdb_client import OMDBClient

Client = OMDBClient()

movie = Client.get_movie("tt0114709")

print("=" * 60)

print(movie["Title"])

print(movie["Year"])

print(movie["Genre"])

print(movie["Director"])

print(movie["Actors"])

print(movie["imdbRating"])

print(movie["imdbVotes"])

print(movie["BoxOffice"])

print("=" * 60)