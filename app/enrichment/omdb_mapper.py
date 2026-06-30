"""
OMDb Mapper

Converts OMDb API responses into OMDbMovie objects.
"""

from app.enrichment.omdb_models import OMDbMovie


class OMDbMapper:
    """
    Maps raw OMDb JSON into OMDbMovie objects.
    """

    def map_movie(
        self,
        data: dict
    ) -> OMDbMovie:
        """
        Convert an OMDb API response into an OMDbMovie.
        """

        return OMDbMovie(

            imdb_id=data["imdbID"],

            title=data["Title"],

            year=data.get("Year"),

            rated=data.get("Rated"),

            released=data.get("Released"),

            runtime=data.get("Runtime"),

            genre=[
                item.strip()
                for item in data.get(
                    "Genre",
                    ""
                ).split(",")
                if item.strip()
            ],

            director=[
                item.strip()
                for item in data.get(
                    "Director",
                    ""
                ).split(",")
                if item.strip()
            ],

            writer=[
                item.strip()
                for item in data.get(
                    "Writer",
                    ""
                ).split(",")
                if item.strip()
            ],

            actors=[
                item.strip()
                for item in data.get(
                    "Actors",
                    ""
                ).split(",")
                if item.strip()
            ],

            plot=data.get("Plot"),

            language=[
                item.strip()
                for item in data.get(
                    "Language",
                    ""
                ).split(",")
                if item.strip()
            ],

            country=[
                item.strip()
                for item in data.get(
                    "Country",
                    ""
                ).split(",")
                if item.strip()
            ],

            awards=data.get("Awards"),

            poster=data.get("Poster"),

            metascore=(
                int(data["Metascore"])
                if data.get("Metascore", "N/A").isdigit()
                else None
            ),

            imdb_rating=(
                float(data["imdbRating"])
                if data.get("imdbRating") not in (
                    None,
                    "N/A"
                )
                else None
            ),

            imdb_votes=(
                int(
                    data["imdbVotes"].replace(
                        ",",
                        ""
                    )
                )
                if data.get("imdbVotes") not in (
                    None,
                    "N/A"
                )
                else None
            ),

            box_office=data.get("BoxOffice"),

            production=data.get("Production"),

            website=data.get("Website")
        )