from pathlib import Path

from app.data.loaders.chunk_loader import ChunkLoader
from app.features.movie_feature_builder import MovieFeatureBuilder
from app.features.feature_writer import FeatureWriter

loader = ChunkLoader(
    Path("data/raw/movielens/ratings.csv"),
    chunk_size=100_000
)

builder = MovieFeatureBuilder()

chunk = next(loader.read())

builder.process_chunk(chunk)

print(f"Movies Tracked: {len(builder.movie_statistics)}")

first_movie = next(iter(builder.movie_statistics))

print(first_movie)

print(builder.movie_statistics[first_movie])

df = builder.finalize()

print()

print(df.head())

print()

print(df.shape)

print()

print(df.columns.tolist())

writer = FeatureWriter(
    Path("data/features")
)

writer.save_parquet(
    df,
    "movie_features.parquet"
)

writer.save_csv(
    df,
    "movie_features.csv"
)