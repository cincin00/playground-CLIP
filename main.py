"""Compatibility entrypoint for ASGI servers that import ``main:app``."""

from app.main import app

__all__ = ["app"]
