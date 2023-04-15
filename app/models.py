from pydantic import BaseModel


class LoveLingo(BaseModel):
    id: int
    content: str
    type: str
