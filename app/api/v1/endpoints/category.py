"""Category endpoints."""

from fastapi import APIRouter

from app.domain.category.schemas import CategoryListResponse
from app.domain.category.service import CategoryService

router = APIRouter()


@router.get("", response_model=CategoryListResponse)
def list_categories() -> CategoryListResponse:
    service = CategoryService()
    return CategoryListResponse(items=service.list_categories())
