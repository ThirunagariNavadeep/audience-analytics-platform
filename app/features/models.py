"""
Feature Models

Dataclasses used during feature engineering.
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

