"""Image search repository."""

from app.domain.image_search.schemas import ImageSearchResult


class ImageSearchRepository:
    def search_by_vector(
        self,
        vector: list[float],
        top_k: int,
        category_id: str | None = None,
    ) -> list[ImageSearchResult]:
        return []
