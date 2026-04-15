"""Product service."""

from app.domain.product.repository import ProductRepository
from app.domain.product.schemas import Product


class ProductService:
    def __init__(self, repository: ProductRepository | None = None) -> None:
        self._repository = repository or ProductRepository()

    def list_products(self) -> list[Product]:
        return self._repository.list_products()
