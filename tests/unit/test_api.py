from fastapi import FastAPI

from app.api.v1.endpoints.category import list_categories
from app.api.v1.endpoints.image_search import search_similar_products
from app.api.v1.endpoints.product import list_products
from app.domain.image_search.schemas import ImageSearchRequest


def test_expected_routes_are_registered(app_instance: FastAPI) -> None:
    paths = {route.path for route in app_instance.routes}

    assert "/health" in paths
    assert "/api/v1/products" in paths
    assert "/api/v1/categories" in paths
    assert "/api/v1/image-search" in paths


def test_product_list_endpoint() -> None:
    response = list_products()

    assert response.model_dump() == {"items": []}


def test_category_list_endpoint() -> None:
    response = list_categories()

    assert response.model_dump() == {"items": []}


def test_image_search_endpoint() -> None:
    request = ImageSearchRequest(image_url="https://example.com/product.jpg", top_k=5)
    response = search_similar_products(request)

    assert response.model_dump() == {"items": []}
