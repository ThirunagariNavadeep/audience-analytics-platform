"""
Centralized logging configuration.

Every module in the application should use this logger
instead of using print().
"""

import logging
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok = True)

LOG_FILE = LOG_DIR / "application.log"

logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s | %(levelname) -8s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("audience_analytics")