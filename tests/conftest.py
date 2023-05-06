import asyncio

from typing import Any, AsyncGenerator, AsyncIterator, Callable, Generator
from unittest.mock import MagicMock

import pytest
from asgi_lifespan import LifespanManager
from fastapi import FastAPI
from httpx import AsyncClient

from app import create_app


class AsyncMock(MagicMock):
    async def __call__(self, *args: Any, **kwargs: Any) -> Callable[..., Any]:
        return super().__call__(*args, **kwargs)


@pytest.fixture(scope="session")
async def app() -> AsyncGenerator[FastAPI, None]:
    app = create_app()
    yield app


@pytest.fixture(scope="session")
def event_loop() -> Generator[Any, Any, Any]:
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def initialized_app(app: FastAPI) -> AsyncGenerator[Any, Any]:
    async with LifespanManager(app):
        yield app


@pytest.fixture(scope="module")
async def async_client(initialized_app: FastAPI) -> AsyncIterator[AsyncClient]:
    async with AsyncClient(
        app=initialized_app,
        base_url="http://testserver",
        headers={"Content-Type": "application/json"},
    ) as client:
        yield client
