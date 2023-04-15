from typing import Any
from fastapi import APIRouter, Depends
from app.models import LoveLingo
from app.repositories.lovelingo import MemoryLoveLingoRepository

from app.services.lovelingo import LoveLingoService
from app.repositories.lovelingo import lovelingo_table

router = APIRouter()


def lovelingo_service() -> LoveLingoService:
    lovelingo_repo = MemoryLoveLingoRepository(table=lovelingo_table)
    return LoveLingoService(lovelingo_repo)


@router.get("/")
async def root() -> dict[str, Any]:
    return {"message": "Hello World"}


@router.get("/questions", response_model=list[LoveLingo])
async def fetch_questions(
    id: int,
    lovelingo_service: LoveLingoService = Depends(lovelingo_service),
) -> list[LoveLingo]:
    return await lovelingo_service.fetch_lovelingos()
