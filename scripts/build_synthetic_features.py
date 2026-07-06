from app.feature_engineering.synthetic_feature_builder import SyntheticFeatureBuilder 
from app.repository.feature_repository import FeatureRepository 
from app.validation.synthetic_feature_validator import SyntheticFeatureValidator 

def main() -> None:

    repo = FeatureRepository()

    builder = SyntheticFeatureBuilder()

    validator = SyntheticFeatureValidator()

    movies = repo.load_analytics_movies()

    features = builder.build(movies)

    report = validator.validate(features)

    print(report)

    if not report["valid"]:
        raise ValueError("Synthetic Feature Validation Failed.")

    repo.save_parquet(features, "synthetic_features.parquet")

    repo.save_csv(features, "synthetic_features.csv")

    print("\n Synthetic Feature Dataset Created Successfully.")

if __name__ == "__main__":
    main()