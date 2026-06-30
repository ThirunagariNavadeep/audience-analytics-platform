from app.repository.feature_repository import FeatureRepository 
from app.enrichment.omdb_enricher import OMDbEnricher 

repo = FeatureRepository()

analytics = repo.load_analytics_movies()

links = repo.load_processed_links()

enricher = OMDbEnricher()

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