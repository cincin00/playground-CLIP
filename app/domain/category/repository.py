"""Category repository."""

from app.domain.category.schemas import Category


class CategoryRepository:
    def list_categories(self) -> list[Category]:
        return []
