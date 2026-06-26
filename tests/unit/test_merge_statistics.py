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

print(f"Users Tracked: {len(builder.user_statistics)}")

first_user = next(iter(builder.user_statistics))

print()

print(first_user)

print(builder.user_statistics[first_user])