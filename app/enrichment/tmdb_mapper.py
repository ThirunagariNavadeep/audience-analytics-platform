"""
TMDB Mapper

Converts TMDB API responses into TMDBMovie objects.
"""
from app.enrichment.tmdb_models import TMDBMovie

class TMDBMapper:
    """
    Maps raw TMDB JSON into TMDBMovie objects.
    """

    def map_movie(
        self,
        data: dict
    ) -> TMDBMovie:
        """
        Convert a TMDB API response into a TMDBMovie.
        """
        return TMDBMovie(
            tmdb_id = data["id"],
            title = data["title"],
            release_date = data.get("release_date"),
            runtime = data.get("runtime"),
            budget = data.get("budget"),
            revenue = data.get("revenue"),
            popularity = data.get("popularity"),
            vote_average = data.get("vote_average"),
            vote_count = data.get("vote_count"),
            original_language = data.get("original_language"),
            status = data.get("status"),
            homepage = data.get("homepage"),
            imdb_id = data.get("imdb_id"),
            belongs_to_collection = (
                data["belongs_to_collection"]["name"]
                if data.get("belongs_to_colection")
                else None
            ),

        genres = [
            genre["name"]
            for genre in data.get("genres", [])
        ],

        production_companies = [
            company["name"]
            for company in data.get("production_companies", [])
        ],

        production_countries = [
            country["name"]
            for country in data.get("production_countries", [])
        ],

        spoken_languages = [
            language["english_name"]
            for language in data.get("spoken_languages", [])
        ],

    )


        