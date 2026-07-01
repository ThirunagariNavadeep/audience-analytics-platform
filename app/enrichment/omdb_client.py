from pathlib import Path 
from typing import Any
import json
import requests
from app.core.config import settings
from app.core.logging import logger

class OMDBClient:
    def __init__(self) -> None:
        self.base_url = settings.OMDB_BASE_URL

        self.api_key = settings.OMDB_API_KEY

        self.cache_dir = Path("data/cache/omdb")

        self.cache_dir.mkdir(
            parents = True,
            exist_ok = True
        ) 

    def get_movie(
        self,
        imdb_id: str,
        use_cache: bool = True
    ) -> dict[str, Any]:
        """
        Retrieve movie details from OMDB.
        """

        cache_file = (
            self.cache_dir / f"{imdb_id}.json"
        )

        if (
            use_cache and cache_file.exists()
        ):

            logger.info(f"Loading OMDB movie {imdb_id} from cache")

            with cache_file.open(
                "r",
                encoding = "utf-8"
            ) as file:

                return json.load(file)

        logger.info(f"Fetching OMDB movie {imdb_id}")

        response = requests.get(
            self.base_url,
            params = {
                "apikey": self.api_key,
                "i": imdb_id
            },
            timeout = 30
        )

        response.raise_for_status()
        data = response.json()

        if data.get("Response") == "False":
            raise ValueError(
                data.get(
                    "Error",
                    "Unknown OMDB error"
                )
            )

        with cache_file.open(
            "w",
            encoding = "utf-8"
        ) as file:

            json.dump(
                data,
                file,
                ensure_ascii = False,
                indent = 4
            )

        return data
