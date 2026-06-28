from app.repository.feature_repository import FeatureRepository
from app.enrichment.tmdb_enricher import TMDBEnricher
from app.enrichment.tmdb_validator import TMDBValidator

repo = FeatureRepository()

analytics = repo.load_analytics_movies()

links = repo.load_processed_links()

enricher = TMDBEnricher()

tmdb = enricher.enrich(
    analytics,
    links,
    limit=100
)

validator = TMDBValidator()

report = validator.validate(
    tmdb
)

print(report)