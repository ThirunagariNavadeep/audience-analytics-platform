from app.core.logging import logger
from app.core.constants import PROCESSED_DATA_DIR
from app.data.loaders.movielens_loader import MovieLensLoader 
from app.data.validators.movielens_validator import MovieLensValidator 
from app.data.transformers.movielens_transformer import MovieLensTransformer 

def main():
    logger.info(
        "Starting MovieLens ETL Pipeline"
    )

    loader = MovieLensLoader()
    validator = MovieLensValidator()
    transformer = MovieLensTransformer()

    movies_df = loader.load_movies()

    validation_results = (
        validator.validate_movies(movies_df)
    )

    if not validation_results["valid"]:
        raise ValueError("Validation Failed")

    movies_clean = (
        transformer.transform(movies_df)
    )

    output_file = (
        PROCESSED_DATA_DIR / "movies_clean.parquet"
    )

    movies_clean.to_parquet(output_file, index=False)

    logger.info(f"Saved processed dataset: {output_file}")

if __name__ == "__main__":
    main()