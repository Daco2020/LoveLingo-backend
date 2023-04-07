# LoveLingo-backend/app/views

## 개요
- `main.py` 를 `app/views` 경로로 이동합니다.
- `main.py` 에 연습용 API를 구현합니다.
- `dev` 폴더와 `run-server.sh` 스크립트를 생성합니다.

<br><br>

## `main.py` 를 `app/views` 경로로 이동하기

<br>

`app` 디렉토리와 그 하위에 `views` 디렉토리를 생성합니다.  
각 디렉토리에는 `__init__.py` 를 생성합니다.

```
__init__.py는 파이썬 패키지의 초기화 스크립트입니다. 패키지를 import할 때 자동으로 실행되며, 패키지에 필요한 초기화 작업을 수행할 수 있습니다.

__init__.py 파일이 없는 경우, 해당 디렉토리는 단순한 디렉토리로 간주됩니다. 반면 __init__.py 파일이 존재하는 디렉토리는 파이썬 패키지로 간주되며, 패키지 내부에 있는 모듈들을 다른 모듈에서 import할 수 있습니다.
```

기존 `main.py` 을 `views` 디렉토리로 이동합니다.

<br><br>

## `main.py` 에 연습용 API 구현하기

<br>

아래 코드를 입력해주세요.
```py
# main.py


from typing import Any
from fastapi import Body, FastAPI


from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root() -> dict[str, Any]:
    return {"message": "Hello World"}


# path parameter 를 사용한 GET API.
@app.get("/path-items/{item_id}")
async def read_item_by_path(item_id: int) -> dict[str, Any]:
    return {"item_id": item_id}


# query parameter 를 사용한 GET API.
@app.get("/query-items/")
async def read_item_by_query(item_id: int) -> dict[str, Any]:
    return {"item_id": item_id}


class Item(BaseModel):
    id: int
    name: str


# BaseModel 을 사용한 POST API.
@app.post("/model-items/")
async def create_item_by_model(item: Item) -> Item:
    return item


# body 를 사용한 POST API.
@app.post("/body-items/")
async def create_item_by_body(
    id: int = Body(embed=True), name: str = Body(embed=True)
) -> dict[str, Any]:
    item = {"id": id, "name": name}
    return item

```

<br>

아래 명령어를 통해 서버를 실행시키고 [OpenAPI 문서](http://127.0.0.1:8000/docs)를 확인합니다.
```
uvicorn app.views.main:app --reload
```
디렉토리가 변경되었기 때문에 서버 실행 명령어 또한 길어졌습니다.  
쉽게 서버를 실행시키기 위하여 스크립트 파일을 생성하겠습니다.

API 구현에 대한 자세한 설명은 [공식문서](https://fastapi.tiangolo.com/tutorial/path-params/)를 참고해주세요.


<br><br>

## `dev` 폴더와 `run-server.sh` 스크립트 생성하기

<br>

루트 디렉토리에서 `dev` 폴더를 생성합니다.  
`dev` 폴더 안에 `run-server.sh` 스크립트 파일을 생성합니다.

<br>

스크립트 파일에는 서버를 실행시키는 명령어를 넣습니다.
```
#!/bin/bash

uvicorn app.views.main:app --reload
```
*`#!/bin/bash` 를 사용하는 이유는 스크립트를 실행할 때 Bash 셸을 사용하도록 보장하기 위해서입니다. Bash는 다양한 기능과 사용성을 제공하며, 스크립트에서 변수, 제어 구조, 함수 등을 사용할 수 있습니다. 

<br>

스크립트를 실행하기 전에 다음 명령어로 실행 권한을 부여합니다.
```
chmod +x dev/*
```

<br>

아래 명령어로 스크립트를 실행시키고 [OpenAPI 문서](http://127.0.0.1:8000/docs)를 확인합니다.
```
dev/run-server.sh
```

