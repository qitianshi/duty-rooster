"""Environment variables and secrets."""

# Copyright 2024 Qi Tianshi. All rights reserved.


from enum import Enum
from os import getenv


class Environment(Enum):
    """Environments; either production or development."""

    PROD = "production"
    DEV = "development"


# See .env.example for environment variable docs.
ENV: Environment = Environment(getenv("ENV"))
GCP_APP_ENDPOINT: str | None = getenv("GCP_APP_ENDPOINT")
PORT: int = int(getenv("PORT", "8080"))                     # Set by Docker.
PROD_BOT_TOKEN: str | None = getenv("PROD_BOT_TOKEN")
TEST_BOT_TOKEN: str | None = getenv("TEST_BOT_TOKEN")
