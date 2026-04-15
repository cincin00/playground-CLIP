"""Product models."""

from dataclasses import dataclass


@dataclass(frozen=True)
class ProductRecord:
    id: str
    name: str
    brand: str | None = None
    category_id: str | None = None
    image_url: str | None = None
    price: int | None = None
