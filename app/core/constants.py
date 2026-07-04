from pathlib import Path 

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
FEATURES_DATA_DIR = DATA_DIR / "features"
MODELS_DIR = DATA_DIR / "models"
EXPORTS_DIR = DATA_DIR / "exports"

LOGS_DIR = PROJECT_ROOT / "logs"
DOCS_DIR = PROJECT_ROOT / "docs"

MOVIELENS_FOLDER = "movielens"
TMDB_FOLDER = "tmdb"
IMDB_FOLDER = "imdb"
SYNTHETIC_FOLDER = "synthetic"

MOVIES_FILE = "movies.csv"
RATINGS_FILE = "ratings.csv"
LINKS_FILE = "links.csv"
TAGS_FILE = "tags.csv"

RANDOM_STATE = 42
TEST_SIZE = 0.20
VALIDATION_SIZE = 0.20

HIGH_RATING_THRESHOLD = 4.0

DEFAULT_SCHEMA = "public"

API_VERSION = "v1"

LOGGER_NAME = "audience_analytics"

MOVIELENS_DATA_DIR = RAW_DATA_DIR / "movielens"
IMDB_DATA_DIR = RAW_DATA_DIR / "imdb"
TMDB_DATA_DIR = RAW_DATA_DIR / "tmdb"
SYNTHETIC_DATA_DIR = RAW_DATA_DIR / "synthetic"
