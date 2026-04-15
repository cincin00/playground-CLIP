"""Image search use cases."""

from app.domain.image_search.schemas import ImageSearchRequest, ImageSearchResult
from app.domain.image_search.service import ImageSearchService


class SearchSimilarProductsUseCase:
    def __init__(self, service: ImageSearchService | None = None) -> None:
        self._service = service or ImageSearchService()

    def execute(self, request: ImageSearchRequest) -> list[ImageSearchResult]:
        return self._service.search(request)
