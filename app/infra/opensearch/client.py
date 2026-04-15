"""OpenSearch client."""

from typing import Any

from app.core.config import Settings, get_settings


def create_opensearch_client(settings: Settings | None = None) -> Any:
    from opensearchpy import OpenSearch

    app_settings = settings or get_settings()
    return OpenSearch(hosts=[app_settings.opensearch_host])
