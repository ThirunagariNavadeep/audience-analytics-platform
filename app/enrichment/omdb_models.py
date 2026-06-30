"""
OMDb Data Models

Defines the data structures used for OMDb enrichment.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class OMDbMovie:
    """
    Represents a movie returned by the OMDb API.
    """

    imdb_id: str

    title: str

    year: str | None = None

    rated: str | None = None

    released: str | None = None

    runtime: str | None = None

    genre: list[str] | None = None

    director: list[str] | None = None

    writer: list[str] | None = None

    actors: list[str] | None = None

    plot: str | None = None

    language: list[str] | None = None

    country: list[str] | None = None

    awards: str | None = None

    poster: str | None = None

    metascore: int | None = None

    imdb_rating: float | None = None

    imdb_votes: int | None = None

    box_office: str | None = None

    production: str | None = None

    website: str | None = None


