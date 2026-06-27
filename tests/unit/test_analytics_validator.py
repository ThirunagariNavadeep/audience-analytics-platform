from app.repository.feature_repository import FeatureRepository
from app.validation.analytics_validator import AnalyticsValidator

repo = FeatureRepository()

analytics = repo.load_analytics_movies()

validator = AnalyticsValidator()

report = validator.validate(analytics)

print(report)