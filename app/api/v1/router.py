"""API v1 router."""

from fastapi import APIRouter

from app.api.v1.endpoints import category, image_search, product

api_router = APIRouter()
api_router.include_router(product.router, prefix="/products", tags=["products"])
api_router.include_router(category.router, prefix="/categories", tags=["categories"])
api_router.include_router(image_search.router, prefix="/image-search", tags=["image-search"])
