"""Product use cases."""

from app.domain.product.schemas import Product
from app.domain.product.service import ProductService


class ListProductsUseCase:
    def __init__(self, service: ProductService | None = None) -> None:
        self._service = service or ProductService()

    def execute(self) -> list[Product]:
        return self._service.list_products()
