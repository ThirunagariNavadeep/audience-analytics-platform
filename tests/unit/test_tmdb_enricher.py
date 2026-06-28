from app.repository.feature_repository import FeatureRepository 
from app.enrichment.tmdb_enricher import TMDBEnricher

repo = FeatureRepository()

analytics = repo.load_analytics_movies()

links = repo.load_processed_links()

enricher = TMDBEnricher()

df = enricher.enrich(
    analytics,
    links,
    limit = 100
)

print(df.head())

print()

print(df.shape)

print()

print(df.columns.tolist())