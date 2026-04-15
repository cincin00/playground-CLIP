"""Image search schemas."""

from pydantic import BaseModel, Field, model_validator

from app.domain.product.schemas import Product


class ImageSearchRequest(BaseModel):
    image_url: str | None = None
    top_k: int = Field(default=10, ge=1, le=100)
    category_id: str | None = None

    @model_validator(mode="after")
    def validate_search_source(self) -> "ImageSearchRequest":
        if not self.image_url:
            msg = "image_url is required until file upload support is implemented"
            raise ValueError(msg)
        return self


class ImageSearchResult(BaseModel):
    product: Product
    score: float = Field(ge=0.0)


class ImageSearchResponse(BaseModel):
    items: list[ImageSearchResult] = Field(default_factory=list)
