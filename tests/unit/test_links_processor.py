from pathlib import Path 
from app.data.processors.links_processor import LinksProcessor

processor = LinksProcessor(
    input_file = Path("data/raw/movielens/links.csv"),
    output_dir = Path("data/processed")
)

links = processor.process()

print(links.head())

print()

print(links.shape)

print()

print(links.dtypes)
