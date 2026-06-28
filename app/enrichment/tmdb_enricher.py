"""
TMDB Enricher

Enriches the analytics movie dataset
with metadata from TMDB.
"""

import pandas as pd

from app.core.logging import logger
from app.enrichment.tmdb_client import TMDBClient
from app.enrichment.tmdb_mapper import TMDBMapper


class TMDBEnricher:
    """
    Enrich analytics dataset with TMDB metadata.
    """

    def __init__(self) -> None:

        self.client = TMDBClient()

        self.mapper = TMDBMapper()

    def enrich(
        self,
        analytics: pd.DataFrame,
        links: pd.DataFrame,
        limit: int | None = 10
    ) -> pd.DataFrame:

        logger.info(
            "Starting TMDB enrichment"
        )

        merged = analytics.merge(
            links,
            on="movie_id",
            how="left"
        )

        merged = merged.dropna(
            subset=["tmdb_id"]
        )

        if limit is not None:

            merged = merged.head(limit)

        enriched_rows = []

        for row in merged.itertuples(index=False):

            tmdb_json = self.client.get_movie(
                int(row.tmdb_id)
            )

            movie = self.mapper.map_movie(
                tmdb_json
            )

            enriched_rows.append({

                **row._asdict(),

                "runtime": movie.runtime,

                "budget": movie.budget,

                "revenue": movie.revenue,

                "popularity": movie.popularity,

                "vote_average_tmdb": movie.vote_average,

                "vote_count_tmdb": movie.vote_count,

                "original_language": movie.original_language,

                "status": movie.status,

                "homepage": movie.homepage,

                "imdb_id": movie.imdb_id,

                "collection": movie.belongs_to_collection,

                "tmdb_genres": movie.genres,

                "production_companies": movie.production_companies,

                "production_countries": movie.production_countries,

                "spoken_languages": movie.spoken_languages
            })

        enriched = pd.DataFrame(
            enriched_rows
        )

        logger.info(
            f"Enriched {len(enriched):,} movies"
        )

        return enriched