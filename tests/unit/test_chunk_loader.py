from app.data.loaders.chunk_loader import ChunkLoader
from pathlib import Path 

loader = ChunkLoader(
    Path("data/raw/movielens/ratings.csv"),
    chunk_size=100_000
  
)

print(loader.get_metadata())

for index, chunk in enumerate(loader.read(), start = 1):
    print(f"Chunk {index}: {chunk.shape}")

    if index == 3:
        break