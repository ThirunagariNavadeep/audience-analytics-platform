from pathlib import Path 
from app.data.loaders.base_loader import BaseDataLoader

class DummyLoader(BaseDataLoader):
    def load(self):
        return None

    def summary(self):
        return {}

loader = DummyLoader(Path("data/raw"))

print(loader.validate_path())