from pydantic import BaseModel


class LoveLingoChoice(BaseModel):
    content: str
    love_lingo_id: int


class LoveLingo(BaseModel):
    id = int
    type = str
    name = str
    description = str
