# 커리큘럼 1차시
- **기술 스택**: Python, FastAPI, Uvicorn
- **학습 목표**:
    - **Python 및 FastAPI 설치**: 학습자는 Python 환경 설정 및 FastAPI 설치 과정을 학습하게 됩니다. VSCode 같은 개발 도구의 기본 설정도 함께 진행합니다.
    - **FastAPI의 기본 구조 이해**: FastAPI가 어떻게 요청을 처리하고, 경로(route)를 설정하는지, 그리고 요청 데이터를 처리하는 방법을 이해합니다.
    - **Uvicorn 서버 실행**: FastAPI 애플리케이션을 실행하기 위해 Uvicorn을 사용하고, 이를 통해 로컬 서버에서 API를 테스트하는 방법을 배웁니다.
- **실습 내용**:
    - **"Hello World" API 작성**: 간단한 FastAPI 프로젝트를 생성하여 "Hello World" 메시지를 반환하는 엔드포인트를 작성합니다.
    - **Path 및 Query Parameters 사용**: 경로 매개변수와 쿼리 매개변수를 사용하여 계산기 API를 만들어, 숫자 두 개를 받아 더하거나 빼는 기능을 구현합니다.
    - **Pydantic을 사용한 데이터 유효성 검사**: Pydantic 모델을 사용해 API 요청 데이터를 유효성 검사하고, 잘못된 입력에 대해 적절한 오류 메시지를 반환하는 방법을 학습합니다.

### FastAPI, Uvicorn 설치
``` shell
pip install fastapi
pip install uvicorn
```

### main.py
``` python
from fastapi import FastAPI # fastapi 클래스를 불러옵니다. 

app = FastAPI() # FastAPI 클래스를 바탕으로 app이란 인스턴스를 만듭니다. 


@app.get("/") # GET 메소드로 가장 루트 url로 접속할 경우
async def root(): # root() 함수를 실행하고
    return {"message": "Hello World"} # Hello World란 메시지 반환합니다.
```

### main 실행
``` Shell
uvicorn main:app --reload
```
쉘에서 다음을 입력하면 서버가 실행된다.

``` Shell
uvicorn main:app -host 0.0.0.0 -port 8001 -reload -workers 4
```
- main:app
  main.py에 있는 app 객체 실행
- -host 0.0.0.0
  서비스 할 웹 주소
  0.0.0.0이면 모든 ip로부터 request 받을 수 있다.
- -port 8000
  서비스를 8000포트를 통해 연다.
- -reload
  서버 실행 파일이 수정되면 서버 자동 재시작
- workers 4
  4개의 프로세스를 미리 구동해, 동시에 4개의 request를 처리할 수 있게 한다.


``` python
import uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
또는 main.py 위 코드를 적으면 .py를 실행하면서 같이 열린다.

http://127.0.0.1:8000/docs 에서 대화형 API 문서를 확인할 수 있다.
http://127.0.0.1:8000/redoc 에서 Alternative API 문서를 확인할 수 있다.

### 덧셈, 뺄셈 계산기 만들기
**Path 및 Query Parameters 사용**
쿼리는 URL에서 `?` 후에 나오고 `&`으로 구분되는 키-값 쌍의 집합이다.
쿼리 매개변수의 타입을 지정하면, 해당 타입으로 변환 및 검증된다. (pydantic에 의해)
Pydantic은 Python에서 데이터의 유효성을 검사하고 타입을 보장하기 위한 강력한 도구이다.
``` python
@app.get("/calculate/{operation}")
async def calculate(operation : str, num1 : float, num2 : float):
	if operation == "add":
		result = num1 + num2
	elif operation == "substract":
		result = num1 - num2
	else:
		return {"error" : "Invalid operation. Please use 'add' or 'substract'."}
	return {"operation" : operation, "num1" : num1, "num2" : num2, "result" : result}
```

``` http
http://127.0.0.1:8000/calculate/add?num1=10.1&num2=5
```
- 결과 : {"operation":"add","num1":10.1,"num2":5.0,"result":15.1}

``` http
http://127.0.0.1:8000/calculate/substract?num1=10.1&num2=5
```
- 결과 : {"operation":"substract","num1":10.1,"num2":5.0,"result":5.1}

# Docker 기본 원리, 명령어
Docker는 컨테이너 기반의 애플리케이션 배포 및 관리를 할 수 있는 오픈소스 가상화 플랫폼이다.
컨테이너는 애플리케이션을 실행하기 위한 모든 파일, 라이브러리, 종속성을 하나의 패키지로 묶어 다른 환경에서도 동일하게 동작하도록 한다.
![d11](https://miro.medium.com/max/862/1*wOBkzBpi1Hl9Nr__Jszplg.png)
### 1. 컨테이너(Container)
컨테이너는 애플리케이션과 그 종속성을 격리된 환경에서 실행할 수 있는 가상화된 패키지다. 
호스트 운영체제의 커널을 공유하지만, 애플리케이션은 각자의 독립된 파일 시스템, 네트워크 등을 가진다.
### 2. 이미지(Image)
이미지는 컨테이너를 생성하기 위한 읽기 전용 템플릿이다. (불변함)
이미지에는 애플리케이션이 실행되기 위해 필요한 모든 파일이 있다.
이미지는 여러 계층으로 구성되어 있으며, 각 계층은 이미지 빌드 시의 명령어(예: `RUN`, `COPY`)로 생성된다.
### 3. Docker 엔진(Docker Engine)
Docker 엔진은 Docker의 핵심 요소로, 컨테이너를 생성하고 관리하는 역할을 한다.
Docker 엔진은 클라이언트-서버 아키텍처로 구성되며, 클라이언트는 `docker` 명령어를 통해 서버(Docker 데몬)에 명령을 전달한다.

### 4. Dockerfile
Dockerfile은 이미지를 빌드하기 위한 스크립트다.
Dockerfile에는 이미지를 구성하기 위한 일련의 명령어들이 포함되어 있다.
예를 들어, 애플리케이션 파일을 이미지에 복사하거나, 패키지를 설치하는 명령어 등이 포함된다.

## 1. Docker 이미지 관련 명령어

**이미지 검색**: Docker Hub에서 이미지를 검색
``` bash
docker search [이미지 이름]
```

**이미지 다운로드**: 이미지를 로컬로 다운로드
``` bash
docker pull [이미지 이름]
```

**이미지 목록 확인**: 로컬에 있는 Docker 이미지들을 확인
``` bash
docker images
```

**이미지 삭제**: 로컬에서 이미지를 삭제
``` bash
docker rmi [이미지 ID]
```

## 2. Docker 컨테이너 관련 명령어

**컨테이너 실행**: 이미지를 기반으로 컨테이너를 생성하고 실행
``` bash
docker run [옵션] [이미지 이름]
```

- `-d`: 백그라운드에서 실행 (Detached mode)
- `-p [호스트 포트]:[컨테이너 포트]`: 포트 포워딩 설정
- `--name [컨테이너 이름]`: 컨테이너 이름 설정
- `-v [호스트 경로]:[컨테이너 경로]`: 볼륨 마운트 설정

**실행 중인 컨테이너 목록 확인**: 현재 실행 중인 컨테이너를 확인
``` bash
docker ps
```

**모든 컨테이너 목록 확인**: 중지된 컨테이너를 포함한 모든 컨테이너를 확인
``` bash
docker ps -a
```

**컨테이너 중지**: 실행 중인 컨테이너를 중지
``` bash
docker stop [컨테이너 ID 또는 이름]
```

**컨테이너 시작**: 중지된 컨테이너를 다시 시작
``` bash
docker start [컨테이너 ID 또는 이름]
```

**컨테이너 삭제**: 컨테이너를 삭제
``` bash
docker rm [컨테이너 ID 또는 이름]
```

**컨테이너 접속**: 실행 중인 컨테이너에 접속하여 명령어를 실행
``` bash
docker attach [컨테이너 ID 또는 이름]
```

# Docker를 이용한 FastAPI 앱 패키징 (with GPT)
FastAPI 서버를 Docker로 실행하려면 다음 단계를 따르면 됩니다. 아래는 FastAPI 애플리케이션을 Docker로 컨테이너화하는 과정입니다.

### 1. FastAPI 애플리케이션 준비
먼저 FastAPI 애플리케이션을 작성합니다. 예를 들어 `app/main.py` 파일에 간단한 FastAPI 애플리케이션을 작성할 수 있습니다.

```python
# app/main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```

### 2. `requirements.txt` 작성
FastAPI와 Uvicorn과 같은 필요한 라이브러리를 명시한 `requirements.txt` 파일을 작성합니다.

```plaintext
# requirements.txt
fastapi
uvicorn
```

### 3. Dockerfile 작성
다음으로 Docker 이미지를 빌드하기 위한 `Dockerfile`을 작성합니다. 이 파일에는 Python 베이스 이미지에서 FastAPI 애플리케이션을 어떻게 설정하고 실행할지에 대한 명령이 포함됩니다.

```Dockerfile
# Dockerfile

# Python 3.9 베이스 이미지 사용
FROM python:3.9-slim

# 작업 디렉터리 설정
WORKDIR /app

# 종속성 파일을 컨테이너에 복사
COPY requirements.txt .

# 종속성 설치
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드를 컨테이너에 복사
COPY . .

# Uvicorn 서버 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 4. Docker 이미지 빌드
이제 Docker 이미지를 빌드합니다. 터미널에서 프로젝트의 루트 디렉토리(예: `app/` 폴더가 있는 곳)로 이동한 후 다음 명령어를 실행합니다.

```bash
docker build -t my-fastapi-app .
```

이 명령은 현재 디렉토리에 있는 `Dockerfile`을 기반으로 `my-fastapi-app`이라는 이름의 Docker 이미지를 생성합니다.

### 5. Docker 컨테이너 실행
이미지를 빌드한 후, Docker 컨테이너를 실행합니다. 다음 명령어를 사용하면 Docker 컨테이너를 백그라운드에서 실행하고 로컬 포트 8000을 컨테이너의 포트 8000과 연결합니다.

```bash
docker run -d -p 8000:8000 my-fastapi-app
```

이 명령어의 의미:
- `-d`: 컨테이너를 백그라운드에서 실행 (Detached mode)
- `-p 8000:8000`: 호스트의 8000번 포트를 컨테이너의 8000번 포트와 연결
- `my-fastapi-app`: 실행할 Docker 이미지 이름

### 6. FastAPI 서버에 접근
컨테이너가 성공적으로 실행되면 로컬 브라우저에서 `http://localhost:8000`에 접속하여 FastAPI 애플리케이션을 확인할 수 있습니다. 

- **API 문서 확인**: `http://localhost:8000/docs`에서 FastAPI의 자동 생성된 Swagger UI 문서를 확인할 수 있습니다.
- **JSON 문서 확인**: `http://localhost:8000/redoc`에서 ReDoc 문서를 확인할 수 있습니다.

### 7. Docker Compose 사용 (선택 사항)
복잡한 설정에서는 `docker-compose`를 사용하여 여러 컨테이너를 관리할 수 있습니다. 간단한 예시로 `docker-compose.yml` 파일을 작성할 수 있습니다.

```yaml
# docker-compose.yml

version: '3.8'

services:
  fastapi:
    build: .
    ports:
      - "8000:8000"
```

이 파일을 사용하면 다음 명령어로 서비스를 시작할 수 있습니다.

```bash
docker-compose up -d
```

이 명령어는 Docker Compose를 사용하여 서비스를 정의된 대로 실행하고, 필요한 모든 컨테이너를 시작합니다.

이렇게 하면 FastAPI 애플리케이션이 Docker 컨테이너에서 실행되며, Docker의 모든 이점을 활용할 수 있습니다.
# ML service clone coding

# 참고 자료
[Python FastAPI 설치하기](https://velog.io/@munang/Python-FastAPI-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0)
[FastAPI Fisrt Steps](https://fastapi.tiangolo.com/tutorial/first-steps/)
[정말 빠른 FastAPI](https://wikidocs.net/162345)
[FastAPI의 구동 방법](https://blog.naver.com/sakpung1004/222907190439)
[FastAPI 배우기](https://fastapi.tiangolo.com/ko/learn/)
[Docker(도커) 시작하기, 설치부터 배포까지](https://zinirun.github.io/2020/08/15/how-to-use-docker/)


