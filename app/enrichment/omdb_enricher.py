"""
OMDb Enricher

Enriches the analytics movie dataset
with metadata from OMDb.
"""

import pandas as pd

from app.core.logging import logger
from app.enrichment.omdb_client import OMDBClient
from app.enrichment.omdb_mapper import OMDbMapper


class OMDbEnricher:
    """
    Enrich analytics dataset with OMDb metadata.
    """

    def __init__(self) -> None:

        self.client = OMDBClient()

        self.mapper = OMDbMapper()

    def enrich(
        self,
        analytics: pd.DataFrame,
        links: pd.DataFrame,
        limit: int | None = 100
    ) -> pd.DataFrame:
        """
        Enrich analytics dataset with OMDb metadata.
        """

        logger.info(
            "Starting OMDb enrichment"
        )

        merged = analytics.merge(
            links,
            on="movie_id",
            how="left"
        )

        merged = merged.dropna(
            subset=["imdb_id"]
        )

        if limit is not None:
            merged = merged.head(limit)

        enriched_rows = []

        failed = 0

        for row in merged.itertuples(index=False):

            try:

                imdb_id = f"tt{int(row.imdb_id):07d}"

                logger.info(
                    f"Processing IMDb ID: {imdb_id}"
                )

                omdb_json = self.client.get_movie(
                    imdb_id
                )

                movie = self.mapper.map_movie(
                    omdb_json
                )

                enriched_rows.append({

                    **row._asdict(),

                    "imdb_id": imdb_id,

                    "rated": movie.rated,

                    "released": movie.released,

                    "runtime_omdb": movie.runtime,

                    "genre_omdb": movie.genre,

                    "director": movie.director,

                    "writer": movie.writer,

                    "actors": movie.actors,

                    "plot": movie.plot,

                    "language": movie.language,

                    "country": movie.country,

                    "awards": movie.awards,

                    "poster": movie.poster,

                    "metascore": movie.metascore,

                    "imdb_rating": movie.imdb_rating,

                    "imdb_votes": movie.imdb_votes,

                    "box_office": movie.box_office,

                    "production": movie.production,

                    "website": movie.website

                })

            except Exception as error:

                logger.warning(
                    f"Skipping IMDb ID {row.imdb_id}: {error}"
                )

                failed += 1

                continue

        enriched = pd.DataFrame(
            enriched_rows
        )

        logger.info(
            f"Successfully enriched: {len(enriched_rows):,}"
        )

        logger.info(
            f"Failed enrichments: {failed:,}"
        )

        logger.info(
            f"Final enriched dataset contains {len(enriched):,} movies"
        )

        return enriched