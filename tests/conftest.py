import pytest
from fastapi import FastAPI

from app.main import app


@pytest.fixture
def app_instance() -> FastAPI:
    return app
