from pathlib import Path
from app.data.loaders.chunk_loader import ChunkLoader 
from app.features.feature_writer import FeatureWriter 
from app.features.user_feature_builder import UserFeatureBuilder 

loader = ChunkLoader(
    Path("data/raw/movielens/ratings.csv"),
    chunk_size = 100_000
)

builder = UserFeatureBuilder()

chunk = next(loader.read())

builder.process_chunk(chunk)

user_features = builder.finalize()

writer = FeatureWriter(Path("data/features"))

writer.save_parquet(
    user_features,
    "user_features.parquet"
)

writer.save_csv(
    user_features,
    "user_features.csv"
)