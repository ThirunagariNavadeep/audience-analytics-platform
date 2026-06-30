from app.repository.feature_repository import FeatureRepository
from app.enrichment.omdb_enricher import OMDbEnricher
from app.enrichment.omdb_validator import OMDbValidator

repo = FeatureRepository()

analytics = repo.load_analytics_movies()

links = repo.load_processed_links()

enricher = OMDbEnricher()

df = enricher.enrich(
    analytics,
    links,
    limit = 100
)

validator = OMDbValidator()

report = validator.validate(df)

print(report)

