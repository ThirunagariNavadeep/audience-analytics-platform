"""
Analytics Dataset Pipeline

Builds the analytics-ready movie dataset,
saves it to disk, validates the output,
and prints a pipeline summary.
"""

from pathlib import Path
import time

from app.core.logging import logger
from app.analytics.movie_analytics_builder import MovieAnalyticsBuilder
from app.repository.feature_repository import FeatureRepository
from app.features.feature_writer import FeatureWriter
from app.validation.analytics_validator import AnalyticsValidator


def main() -> None:
    """
    Execute the analytics dataset pipeline.
    """

    logger.info("=" * 70)
    logger.info("Audience Analytics Dataset Pipeline")
    logger.info("=" * 70)

    start_time = time.perf_counter()


    repository = FeatureRepository()

    builder = MovieAnalyticsBuilder()

    writer = FeatureWriter(
        Path("data/analytics")
    )

    validator = AnalyticsValidator()


    logger.info("Loading Processed Movies")

    movies = repository.load_processed_movies()

    logger.info("Loading Movie Features")

    movie_features = repository.load_movie_features()


    analytics_movies = builder.build(
        movies,
        movie_features
    )


    writer.save_parquet(
        analytics_movies,
        "analytics_movies.parquet"
    )

    writer.save_csv(
        analytics_movies,
        "analytics_movies.csv"
    )

  
    report = validator.validate(
        analytics_movies
    )

    logger.info("=" * 70)
    logger.info("Analytics Validation Report")
    logger.info("=" * 70)

    logger.info(
        f"Dataset Valid : {report['valid']}"
    )

    logger.info(
        f"Total Rows : {report['total_rows']:,}"
    )

    logger.info("Errors")

    for key, value in report["errors"].items():

        logger.info(
            f"  {key}: {value}"
        )

    logger.info("Warnings")

    for key, value in report["warnings"].items():

        logger.info(
            f"  {key}: {value}"
        )

   
    elapsed_time = time.perf_counter() - start_time

    logger.info("=" * 70)
    logger.info("Analytics Pipeline Completed Successfully")
    logger.info("=" * 70)

    logger.info(
        f"Movies Processed : {len(analytics_movies):,}"
    )

    logger.info(
        f"Validation Status : {'PASSED' if report['valid'] else 'FAILED'}"
    )

    logger.info(
        f"Execution Time : {elapsed_time:.2f} seconds"
    )

    logger.info("=" * 70)


if __name__ == "__main__":
    main()