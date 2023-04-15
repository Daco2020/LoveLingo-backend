import abc

from app.models import LoveLingo


lovelingo_table: list[LoveLingo] = []


class LoveLingoRepository(abc.ABC):
    @abc.abstractmethod
    async def fetch(self) -> list[LoveLingo]:
        ...


class MemoryLoveLingoRepository(LoveLingoRepository):
    def __init__(self, table: list[LoveLingo]) -> None:
        self._table = table

    async def fetch(self) -> list[LoveLingo]:
        return self._table
