"""
Streaming User Feature Builder

Builds user-level statistics incrementally
from MovieLens ratings data.
"""

import pandas as pd 
from app.core.logging import logger

class UserFeatureBuilder:
    def __init__(self):
        """
        Intialize the feature builder
        """
        self.user_statistics = {}

    def process_chunk(
        self,
        chunk: pd.DataFrame
    ) -> pd.DataFrame:

        """
        Build user statistics for one chunk.

        Returns a summarized DataFrame
        containing one row per user.
        """
        logger.info(f"Processing chunk with {len(chunk):,} rows")

        chunk = chunk.copy()
        chunk["timestamp"] = pd.to_datetime(
            chunk["timestamp"],
            unit = 's'
        )

        chunk_summary = (
            chunk
            .groupby("userId")
            .agg(
                rating_count = ("rating", "count"),
                rating_sum = ("rating", "sum"),
                rating_min = ("rating", "min"),
                rating_max = ("rating", "max"),
                movies_seen = (
                    "movieId",
                    lambda x: set(x)
                ),

                first_timestamp = (
                    "timestamp",
                    "min"
                ),

                last_timestamp = (
                    "timestamp",
                    "max"
                )
            )        
            .reset_index()

            chunk_summary = chunk_summary.rename(
                columns = {
                    "userId": "user_id"
                }
            )
        )

        logger.info(f"Chunk summarized into {len(chunk_summary):,} users")

        return chunk_summary


