from typing import Any
from pydantic import BaseModel


class LoveLingoChoice(BaseModel):
    content: str
    love_lingo_id: int


class LoveLingo(BaseModel):
    id: int
    type: str
    name: str
    description: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "count": 0,
        }
