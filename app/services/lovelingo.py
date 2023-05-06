import random
from typing import Any
from app.models import LoveLingoChoice
from collections import defaultdict
from app.repositories.lovelingo import LoveLingoRepository


class LoveLingoService:
    def __init__(self, lovelingo_repo: LoveLingoRepository):
        self._lovelingo_repo = lovelingo_repo

    async def get_result(self, answers: list[int]) -> list[dict[str, Any]] | None:
        # TODO: validation 함수로 분리하기
        if len(answers) != 15:
            return None

        love_lingos = await self._lovelingo_repo.fetch_love_lingo()
        results = [love_lingo.to_dict() for love_lingo in love_lingos]

        for id in answers:
            for result in results:
                if result["id"] == id:
                    result["count"] += 1
        return results

    async def fetch_choices(self) -> list[tuple[LoveLingoChoice, LoveLingoChoice]]:
        raw_choices = await self._lovelingo_repo.fetch_choices()
        return self._create_choices(raw_choices)

    def _create_choices(
        self,
        raw_choices: list[LoveLingoChoice],
    ) -> list[tuple[LoveLingoChoice, LoveLingoChoice]]:
        love_lingo_id_choices_dict = defaultdict(list)

        for elem in raw_choices:
            love_lingo_id_choices_dict[elem.love_lingo_id].append(elem)

        id_list = [choice.love_lingo_id for choice in raw_choices]
        shuffled_id_list = self._non_consecutive_shuffle(id_list)

        result_tuples = []
        for i in range(0, len(shuffled_id_list), 2):
            # TODO: 한번 사용한 choice 는 제외하도록 보완 필요
            choice1 = [
                choice
                for choice in raw_choices
                if choice.love_lingo_id == shuffled_id_list[i]
            ][0]
            choice2 = [
                choice
                for choice in raw_choices
                if choice.love_lingo_id == shuffled_id_list[i + 1]
            ][0]
            result_tuples.append((choice1, choice2))

        return result_tuples

    def _non_consecutive_shuffle(self, arr):
        random.shuffle(arr)

        def swap_elements(i, j):
            arr[i], arr[j] = arr[j], arr[i]

        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                j = i + 1
                while j < len(arr) and arr[j] == arr[i]:
                    j += 1
                if j < len(arr):
                    swap_elements(i, j)

        return arr
