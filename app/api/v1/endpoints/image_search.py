"""Image search endpoints."""

from fastapi import APIRouter

from app.domain.image_search.schemas import ImageSearchRequest, ImageSearchResponse
from app.domain.image_search.usecase import SearchSimilarProductsUseCase

router = APIRouter()


@router.post("", response_model=ImageSearchResponse)
def search_similar_products(request: ImageSearchRequest) -> ImageSearchResponse:
    usecase = SearchSimilarProductsUseCase()
    return ImageSearchResponse(items=usecase.execute(request))
