# LoveLingo-backend

## 개요

- `Python` 가상환경을 만들고 종속성 관리 툴을 설치합니다.  
- `FastAPI` 설치 및 API를 만들고 서버를 실행합니다.  
- `.gitignore` 파일을 생성하여 불필요한 파일 업로드를 막습니다.  
- `pre-commit` 로 commit 시 코드 스타일과 정적 검사를 자동화합니다.

<br><br>

## 개발환경 세팅하기

<br>

### 가상환경 만들기

<br>

Pyenv 설치 - Pyenv는 다른 버전의 Python 간에 쉽게 전환할 수 있는 Python 버전 관리 도구입니다.
```
curl https://pyenv.run | bash
```

<br>

Python 설치 - Pyenv가 설치되면 이를 사용하여 개발 환경에 사용할 특정 버전의 Python을 설치할 수 있습니다.
```
pyenv install 3.10.6
```

<br>

가상환경 생성 - 명령어 'pyenv virtualenv {`설치한 Python 버전`} {`가상환경 이름`}' 를 통해 가상환경을 생성할 수 있습니다.
```
pyenv virtualenv 3.10.6 lovelingo
```

<br>

가상환경 진입 - 명령어 'pyenv activate {`가상환경 이름`}' 를 통해 가상환경으로 진입할 수 있습니다.
```
pyenv activate lovelingo
```


<br><br>

### 종속성 관리 툴 설치

<br>

Poetry 설치 - Poetry는 프로젝트의 종속성과 가상 환경을 관리하는 데 도움이 되는 Python용 종속성 관리 도구입니다. 
```
curl -sSL https://install.python-poetry.org | python3 -
```

<br>

Poetry 초기화 - 종속성 관리를 시작하기 위해 Poetry를 초기화합니다. 명령어 입력 후 configure 를 세팅합니다.
```
poetry init
```


<br><br>

### FastAPI 설치 및 server 실행

<br>

FastAPI - Python 기반의 비동기 처리 웹 프레임워크로 OpenAPI 및 JSON 스키마 자동 생성 및 Python 타입 힌트를 통한 입력 데이터 검증을 지원합니다.

uvicorn - FastAPI를 비롯한 ASGI 애플리케이션 실행, 이벤트 루프 및 비동기 I/O를 사용해 높은 성능 보장하는 Python의 ASGI(Asynchronous Server Gateway Interface) 서버입니다.

```
poetry add fastapi uvicorn
```

<br>

main.py 파일을 생성하고 아래 코드를 입력합니다.
```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```

<br>

터미널에서 아래 명령어를 입력해 서버를 실행합니다.
```
uvicorn main:app --reload
```

<br>

웹 브라우저 http://127.0.0.1:8000/ 로 접속하여 "Hello World" 메시지를 확인합니다.
```
{"message":"Hello World"}
```

<br>

웹 브라우저 http://127.0.0.1:8000/docs 로 접속하여 OpenAPI 가 생성되었는지 확인합니다.

<br><br>

### .gitignore 파일 생성하기

<br>


`.gitignore` 파일은 Git 저장소에 포함되지 않아야 하는 파일들을 지정하는 설정 파일입니다. 보안성을 높이기 위해 인증 정보나 민감한 데이터를 포함한 파일, 불필요한 로그 파일, 컴파일된 바이너리 파일 등 저장소에 저장할 필요가 없는 파일들을 제외하고 Git에 커밋되지 않도록 설정할 수 있습니다.

https://www.toptal.com/developers/gitignore

위 사이트에 접속하여 사용하는 운영체제, 개발 환경, 프로그래밍 언어 등을 입력합니다. 생성 버튼을 누르고 나온 내용을 `.gitignore` 파일에 붙여넣기 합니다.


<br><br>

### pre-commit 설정하기

<br>


`pre-commit`은 Git을 사용하는 개발자들이 코드 커밋 전에 자동으로 실행되는 검사 도구입니다. 이 도구는 코드 스타일, 코드 린트, 정적 분석, 보안 취약점 등을 검사하여 코드 품질을 향상시키고 버그를 예방하는데 도움을 줍니다.
```
poetry add pre-commit --dev
```
*`--dev` 옵션은 dev 환경의 종속성을 의미합니다.

<br>

`.pre-commit-config.yaml` 파일을 생성하여 아래 내용을 입력합니다.
```
repos:
  - repo: https://github.com/psf/black
    rev: 23.3.0
    hooks:
      - id: black

  - repo: https://github.com/charliermarsh/ruff-pre-commit
    rev: v0.0.259
    hooks:
      - id: ruff
      
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.1.1
    hooks:
      - id: "mypy"
```
기재된 repo로부터 hook으로 사용할 패키지를 가져옵니다.

`black` 은 Python 코드 포매터입니다.  
`ruff` 는  Rust로 작성된 Python linter입니다.  
`mypy` 는 Python 정적 분석 도구입니다.

<br>

`pre-commit` 설치 - 아래 명령어를 통해 지정된 hook을 활성화합니다.

```
pre-commit install
```

<br>

`git commit` 명령어를 통해 `pre-commit` 이 정상동작하는지 확인합니다.
```
black.........................Passed
ruff..........................Passed
mypy..........................Passed
```