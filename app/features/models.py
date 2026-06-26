"""
Feature Models
"""

from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class UserStatistics:
    """
    Running statistics for one user.
    """

    rating_count: int = 0

    rating_sum: float =  0.0

    rating_min: float = float("inf")

    rating_max: float = float("-inf")

    movies_seen: set[int] = field(default_factory = set)

    first_timestamp: datetime | None = None

    last_timestamp: datetime | None = None

    def average_rating(self) -> float:
        """
        Compute Average Rating
        """

        if self.rating_count == 0:
            return 0.0
        return (
            self.rating_sum / self.rating_count
        )

    def movies_watched(self) -> int:
        """
        Number of Unique Movies
        """

        return len(self.movies_seen)

