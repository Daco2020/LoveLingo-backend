from typing import Any
from fastapi import Body, FastAPI


from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root() -> dict[str, Any]:
    return {"message": "Hello World"}


@app.get("/path-items/{item_id}")
async def read_item_by_path(item_id: int) -> dict[str, Any]:
    return {"item_id": item_id}


@app.get("/query-items/")
async def read_item_by_query(item_id: int) -> dict[str, Any]:
    return {"item_id": item_id}


class Item(BaseModel):
    id: int
    name: str


@app.post("/model-items/")
async def create_item_by_model(item: Item) -> Item:
    return item


@app.post("/body-items/")
async def create_item_by_body(
    id: int = Body(embed=True), name: str = Body(embed=True)
) -> dict[str, Any]:
    item = {"id": id, "name": name}
    return item
