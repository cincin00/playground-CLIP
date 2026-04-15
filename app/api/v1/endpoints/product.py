"""Product endpoints."""

from fastapi import APIRouter

from app.domain.product.schemas import ProductListResponse
from app.domain.product.usecase import ListProductsUseCase

router = APIRouter()


@router.get("", response_model=ProductListResponse)
def list_products() -> ProductListResponse:
    usecase = ListProductsUseCase()
    return ProductListResponse(items=usecase.execute())
