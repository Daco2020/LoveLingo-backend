from typing import Any
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def root() -> dict[str, Any]:
    return {"message": "Hello World"}
