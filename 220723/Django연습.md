# 장고 개발 환경 준비하기

## 파이썬 가상환경 사용해 보기

### 가상 환경 디렉토리 생성하기

가상 환경 폴더를 만들 디렉토리에서 작업

```shell
mkdir venvs
cd venvs
```



### 가상 환경 만들기

- 파이썬 모듈 중 venv 라는 모듈 사용
- mysite는 생성할 가상 환경의 이름
- 명령을 수행하면 venus 디렉토리 아래에 mysite 라는 디렉토리가 생성되어 있음

```shell
python -m venv mysite
```



### 가상 환경에 진입 및 벗어나기

- mysite안의 Scripts 디렉토리의 activate 명령을 수행
- Scripts 디렉토리 안에서 activate 명령이 수행이 안될 경우는 activate가 있는 디렉토리에서 수행(예를들어 bin)

```shell
cd mysite/Scripts
activate
(mysite) /Scripts
```

```shell
deactivate
```



## 장고 설치하기

### 가상 환경에서 장고 설치하기

- 가상 환경에 진입한 상태에서 작업
- pip는 최신 상태로 업데이트

```shell
(mysite)
pip install --upgrade
pip install django==3.1.3
```

# 장고 프로젝트 생성하기

## 프로젝트 디렉토리 생성하기

### 프로젝트 루트 디렉토리 생성하기

- 장고 프로젝트는 여러 개가 될 수 있으므로 프로젝트를 모아 둘 프로젝트 루트 디렉토리 생성은 필수
- 이 작업은 가상 환경이 아닌 로컬에서 수행
- 이하 프로젝트 루트 디렉토리는 projects로 함

```shell
mkdir projects
cd projects
projects >
```



### 프로젝트 루트 디렉토리 안에서 가상 환경 진입하기

- 프로젝트 루트 디렉토리 안에서 명령어를 입력해 앞에서 만든 mysite 가상 환경에 진입

```shell
projects > /venvs/mysite/Scripts/activate
(mysite) projects >
```



### 장고 프로젝트를 담을 디렉토리 생성하고 이동하기

- 장고 프로젝트를 담을 mysite 디렉토리를 생성하고 이동

``` shell
(mysite) projects > mkdir mysite
(mysite) projects > cd mysite
(mysite) projects/mysite >
```



### 장고 프로젝트 생성하기

- 장고 프로젝트 디렉토리에서 django-admin이라는 도구로 장고 프로젝트 생성
- Config 다음에 . 은 현재 디렉토리를 프로젝트 디렉토리로 만들라는 의미

``` shell
(mysite) projects/mysite > django-admin startproject config .
```



### 장고 프로젝트 내용물 확인하기

- 아래와 같은 구조로 파일이 구성되어 있는지 확인

```
|- config/
|    |- asgi.py
|    |- settings.py
|    |- urls.py
|    |- wsgi.py
|    |- __init__.py
|- manage.py
```



## 개발 서버 구동하고 웹 사이트에 접속해 보기

### 개발 서버 구동하기

- python manage.py runserver 명령을 실행하면 개발 서버 구동
- 서버를 종료하려면 ctrl + c 를 누르면 됨
- 서버가 구동되고 있는 상태에서 127.0.0.1:8000에 접속

```shell
(mysite) projects/mysite > python manage.py runserver
```

