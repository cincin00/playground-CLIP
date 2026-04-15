"""Database configuration."""

from app.core.config import Settings, get_settings


def get_database_url(settings: Settings | None = None) -> str:
    return (settings or get_settings()).database_url
