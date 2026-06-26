"""
Build Feature Pipeline

Processes the complete MovieLens ratings dataset
and generates user and movie feature datasets.
"""

from pathlib import Path
import time

from app.core.logging import logger
from app.data.loaders.chunk_loader import ChunkLoader
from app.features.user_feature_builder import UserFeatureBuilder
from app.features.movie_feature_builder import MovieFeatureBuilder
from app.features.feature_writer import FeatureWriter


def main() -> None:
    """
    Execute the complete feature engineering pipeline.
    """

    logger.info("=" * 70)
    logger.info("Audience Analytics Feature Pipeline")
    logger.info("=" * 70)

    start_time = time.perf_counter()

    # Initialize components
    loader = ChunkLoader(
        Path("data/raw/movielens/ratings.csv"),
        chunk_size=100_000
    )

    user_builder = UserFeatureBuilder()

    movie_builder = MovieFeatureBuilder()

    writer = FeatureWriter(
        Path("data/features")
    )

    total_chunks = 0


    for chunk in loader.read():

        total_chunks += 1

        logger.info(
            f"Processing Chunk {total_chunks:,}"
        )

        user_builder.process_chunk(chunk)

        movie_builder.process_chunk(chunk)


    logger.info("Finalizing user features")

    user_features = user_builder.finalize()

    logger.info("Finalizing movie features")

    movie_features = movie_builder.finalize()


    writer.save_parquet(
        user_features,
        "user_features.parquet"
    )

    writer.save_csv(
        user_features,
        "user_features.csv"
    )


    writer.save_parquet(
        movie_features,
        "movie_features.parquet"
    )

    writer.save_csv(
        movie_features,
        "movie_features.csv"
    )

    elapsed_time = time.perf_counter() - start_time

    logger.info("=" * 70)
    logger.info("Pipeline Completed Successfully")
    logger.info("=" * 70)

    logger.info(
        f"Chunks Processed : {total_chunks:,}"
    )

    logger.info(
        f"Users Generated : {len(user_features):,}"
    )

    logger.info(
        f"Movies Generated : {len(movie_features):,}"
    )

    logger.info(
        f"Execution Time : {elapsed_time:.2f} seconds"
    )

    logger.info("=" * 70)


if __name__ == "__main__":
    main()