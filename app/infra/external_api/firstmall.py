"""Firstmall external API client."""

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class FirstmallClientConfig:
    base_url: str
    api_key: str


class FirstmallClient:
    def __init__(self, config: FirstmallClientConfig) -> None:
        self._config = config

    @property
    def config(self) -> FirstmallClientConfig:
        return self._config

    def list_products(self) -> list[dict[str, Any]]:
        msg = "Firstmall product synchronization is not implemented yet"
        raise NotImplementedError(msg)
