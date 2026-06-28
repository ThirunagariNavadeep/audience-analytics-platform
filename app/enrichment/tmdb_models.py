"""
TMDB Data Models

Defines the data structures used for TMDB enrichment.
"""
from dataclasses import dataclass, field

@dataclass(slots = True)
class TMDBMovie:
    """
    Represents a movie returned by the TMDB API.
    """
    tmdb_id: int
    title: str
    release_date: str | None = None
    runtime: int | None = None
    budget: int | None = None
    revenue: int | None = None
    popularity: float | None = None
    vote_average: int | None = None
    vote_count: int | None = None
    original_language: str | None = None
    status: str | None = None
    homepage: str | None = None
    imdb_id: str | None = None
    belongs_to_collection: str | None = None
    genres: list[str] = field(default_factory = list)
    production_companies: list[str] = field(default_factory = list)
    production_countries: list[str] = field(default_factory = list)
    spoken_languages: list[str] = field(default_factory = list)