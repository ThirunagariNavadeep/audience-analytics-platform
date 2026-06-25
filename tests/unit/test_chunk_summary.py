from pathlib import Path 
from app.data.loaders.chunk_loader import ChunkLoader 
from app.features.user_feature_builder import UserFeatureBuilder

loader = ChunkLoader(
    Path("data/raw/movielens/ratings.csv"),
    chunk_size = 100000
)

builder = UserFeatureBuilder()

chunk = next(loader.read())

summary = builder.process_chunk(chunk)

print(summary.head())

print()

print(summary.columns.tolist())

print()

print(summary.shape)