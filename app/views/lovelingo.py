from typing import Any
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.models import LoveLingoChoice
from app.repositories.lovelingo import MemoryLoveLingoRepository

from app.services.lovelingo import LoveLingoService
from app.repositories.lovelingo import choice_table, love_lingo_table

router = APIRouter()


def lovelingo_service() -> LoveLingoService:
    lovelingo_repo = MemoryLoveLingoRepository(love_lingo_table, choice_table)
    return LoveLingoService(lovelingo_repo)


@router.get("/")
async def root() -> dict[str, Any]:
    return {"message": "Hello Love"}


@router.get("/choices", response_model=list[tuple[LoveLingoChoice, LoveLingoChoice]])
async def fetch_choices(
    lovelingo_service: LoveLingoService = Depends(lovelingo_service),
) -> list[tuple[LoveLingoChoice, LoveLingoChoice]]:
    lovelingo = await lovelingo_service.fetch_choices()
    return lovelingo


class Answers(BaseModel):
    answers: list[str]  # ["A", "B", "C", "e", "d"]
    duration_time: str  # 00:15:23


@router.post("/results", response_model=None)
async def get_result(
    answers: Answers,
    lovelingo_service: LoveLingoService = Depends(lovelingo_service),
) -> None:
    await lovelingo_service.get_result()
