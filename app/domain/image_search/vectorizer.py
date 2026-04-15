"""CLIP embedding vectorizer."""

from typing import Protocol


class ImageVectorizer(Protocol):
    def embed_image_url(self, image_url: str) -> list[float]:
        """Return an embedding vector for an image URL."""


class PlaceholderImageVectorizer:
    def embed_image_url(self, image_url: str) -> list[float]:
        return []
