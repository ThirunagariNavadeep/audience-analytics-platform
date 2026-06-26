"""
Movie Feature Models
"""

from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class MovieStatistics:
    """
    Running statistics for one movie.
    """

    rating_count: int = 0

    rating_sum: float = 0.0

    rating_min: float = float("inf")

    rating_max: float = float("-inf")

    unique_users: set[int] = field(default_factory = set)

    first_rating: datetime | None = None

    last_rating: datetime | None = None 

    def average_rating(self) -> float:
        """
        Compute the average rating.
        """
        if self.rating_count == 0:
            return 0.0

        return self.rating_sum / self.rating_count

    def total_users(self) -> int:
        """
        Number of unique users who rated the movie.
        """

        return len(self.unique_users)