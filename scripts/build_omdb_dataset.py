"""
Build OMDb Enriched Dataset
"""
from pathlib import Path 
import time
from app.core.logging import logger
from app.repository.feature_repository import FeatureRepository 
from app.enrichment.omdb_enricher import OMDbEnricher 
from app.enrichment.omdb_validator import OMDbValidator 
from app.features.feature_writer import FeatureWriter 

def main():

    logger.info("-" * 70)
    logger.info("OMDb Dataset Pipeline")
    logger.info("-" * 70)

    start = time.perf_counter()

    repo = FeatureRepository()

    writer = FeatureWriter(Path("data/analytics"))

    logger.info("Loading analytics dataset")

    analytics = repo.load_analytics_movies()

    logger.info("Loading links dataset")

    links = repo.load_processed_links()

    enricher = OMDbEnricher()

    enriched = enricher.enrich(
        analytics,
        links,
        limit = None
    )

    validator = OMDbValidator()

    report = validator.validate(enriched)

    logger.info(report)

    writer.save_parquet(
        enriched,
        "analytics_movies_omdb.parquet"
    )

    writer.save_csv(
        enriched,
        "analytics_movies_omdb.csv"
    )

    elapsed = time.perf_counter() - start

    logger.info("-" * 70)
    logger.info("OMDb Dataset Pipeline Completed")
    logger.info("-" * 70)
    logger.info(f"Movies Processed: {len(enriched):,}")
    logger.info(f"Execution Time: {elapsed:.2f} seconds")
    logger.info("-" * 70)

if __name__ == "__main__":
    main()