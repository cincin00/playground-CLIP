"""Product schemas."""

from pydantic import BaseModel, Field


class Product(BaseModel):
    id: str
    name: str
    brand: str | None = None
    category_id: str | None = None
    image_url: str | None = None
    price: int | None = Field(default=None, ge=0)


class ProductListResponse(BaseModel):
    items: list[Product] = Field(default_factory=list)
