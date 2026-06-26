from pathlib import Path
from app.data.loaders.chunk_loader import ChunkLoader
from app.features.user_feature_builder import UserFeatureBuilder

loader = ChunkLoader(
    Path("data/raw/movielens/ratings.csv"),
    chunk_size = 100_000
)

builder = UserFeatureBuilder()

chunk = next(loader.read())

builder.process_chunk(chunk)

df = builder.finalize()

print(df.head())

print()

print(df.shape)

print()

print(df.columns.tolist())