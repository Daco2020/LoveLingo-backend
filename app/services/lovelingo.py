from app.models import LoveLingo

from app.repositories.lovelingo import LoveLingoRepository


class LoveLingoService:
    def __init__(self, lovelingo_repo: LoveLingoRepository):
        self._lovelingo_repo = lovelingo_repo

    async def fetch_lovelingos(self) -> list[LoveLingo]:
        return await self._lovelingo_repo.fetch()
