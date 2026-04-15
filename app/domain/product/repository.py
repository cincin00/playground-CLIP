"""Product repository."""

from app.domain.product.schemas import Product


class ProductRepository:
    def list_products(self) -> list[Product]:
        return []
