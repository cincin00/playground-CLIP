"""OpenSearch repository."""

from typing import Any

from app.core.config import Settings, get_settings


class OpenSearchVectorRepository:
    def __init__(self, client: Any, settings: Settings | None = None) -> None:
        self._client = client
        self._settings = settings or get_settings()

    def search_products(
        self,
        vector: list[float],
        top_k: int,
        category_id: str | None = None,
    ) -> list[dict[str, Any]]:
        filters: list[dict[str, Any]] = []
        if category_id:
            filters.append({"term": {"category_id": category_id}})

        query: dict[str, Any] = {
            "size": top_k,
            "query": {
                "knn": {
                    self._settings.opensearch_vector_field: {
                        "vector": vector,
                        "k": top_k,
                    },
                },
            },
        }
        if filters:
            query["post_filter"] = {"bool": {"filter": filters}}

        response = self._client.search(index=self._settings.opensearch_index, body=query)
        hits = response.get("hits", {}).get("hits", [])
        return [hit.get("_source", {}) for hit in hits]
