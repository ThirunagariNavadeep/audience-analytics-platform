"""
TMDB Client

Handles communication with The Movie Database (TMDB) API.
"""

from typing import Any
import requests
import os
import json
from app.core.config import settings
from app.core.logging import logger
from pathlib import Path 

class TMDBClient:
    """
    Client for interacting with the TMDB API.
    """

    def __init__(self) -> None:
        self.base_url = settings.TMDB_BASE_URL

        self.headers = {
            "Authorization": f"Bearer {settings.TMDB_READ_ACCESS_TOKEN}",
            "accept": "application/json"
        }

        self.cache_dir = Path("data/cache/tmdb")
        self.cache_dir.mkdir(
            parents = True,
            exist_ok = True
        )

    def get_movie(
        self,
        tmdb_id: int,
        use_cache: bool = True 
    ) -> dict[str, Any]:

        cache_file = self.cache_dir / f"{tmdb_id}.json"

        if cache_file.exists():
            logger.info(f"Loading TMDB movie {tmdb_id} from cache")

            with cache_file.open(
                "r",
                encoding = "utf-8"
            ) as file:

                return json.load(file)
        
        logger.info(f"Fetching TMDB movie {tmdb_id}")

        url = f"{self.base_url}/movie/{tmdb_id}"
        response = requests.get(
            url,
            headers = self.headers,
            timeout = 30
        )

        response.raise_for_status()
        data = response.json()

        with cache_file.open(
            "w",
            encoding = "utf-8"
        )as file:

            json.dump(
                data,
                file,
                ensure_ascii = False,
                indent = 4
            )

        return data