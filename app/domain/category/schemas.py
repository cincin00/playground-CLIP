"""Category schemas."""

from pydantic import BaseModel, Field


class Category(BaseModel):
    id: str
    name: str
    parent_id: str | None = None


class CategoryListResponse(BaseModel):
    items: list[Category] = Field(default_factory=list)
