"""Category service."""

from app.domain.category.repository import CategoryRepository
from app.domain.category.schemas import Category


class CategoryService:
    def __init__(self, repository: CategoryRepository | None = None) -> None:
        self._repository = repository or CategoryRepository()

    def list_categories(self) -> list[Category]:
        return self._repository.list_categories()
