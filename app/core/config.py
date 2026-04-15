"""Application configuration."""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "playground-clip"
    app_env: str = "local"
    app_debug: bool = False
    api_v1_prefix: str = "/api/v1"
    log_level: str = "INFO"

    database_url: str = "sqlite:///./local.db"

    opensearch_host: str = "http://localhost:9200"
    opensearch_index: str = "products"
    opensearch_vector_field: str = "image_vector"
    opensearch_vector_dimension: int = 512

    redis_url: str | None = None

    clip_model_name: str = "ViT-B-32"
    clip_pretrained: str = "laion2b_s34b_b79k"
    clip_device: str = "cpu"

    firstmall_base_url: str | None = None
    firstmall_api_key: str | None = None

    cors_allowed_origins: str = ""

    @property
    def cors_origins(self) -> list[str]:
        if not self.cors_allowed_origins:
            return []
        return [origin.strip() for origin in self.cors_allowed_origins.split(",") if origin.strip()]


@lru_cache
def get_settings() -> Settings:
    return Settings()
