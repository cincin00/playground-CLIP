"""Image search service."""

from app.domain.image_search.repository import ImageSearchRepository
from app.domain.image_search.schemas import ImageSearchRequest, ImageSearchResult
from app.domain.image_search.vectorizer import ImageVectorizer, PlaceholderImageVectorizer


class ImageSearchService:
    def __init__(
        self,
        repository: ImageSearchRepository | None = None,
        vectorizer: ImageVectorizer | None = None,
    ) -> None:
        self._repository = repository or ImageSearchRepository()
        self._vectorizer = vectorizer or PlaceholderImageVectorizer()

    def search(self, request: ImageSearchRequest) -> list[ImageSearchResult]:
        vector = self._vectorizer.embed_image_url(request.image_url or "")
        return self._repository.search_by_vector(
            vector=vector,
            top_k=request.top_k,
            category_id=request.category_id,
        )
