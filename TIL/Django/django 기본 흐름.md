# django 기본 흐름

- url을 정의한다.
- views.py에 실행할 함수를 만든다.
- 반환할 html 파일을 만든다.



- 데이터 관리 - Model
- 인터페이스(화면) - Template
- 중간관리(상호동작) - View



## Django project/app

- Django는 하나의 프로젝트가 복수의 app을 가지는 구조로 되어 있다.



## 프로젝트 기본 설정(urls.py)

- 프로젝트 폴더

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('pages.urls')),
    path('boards/', include('boards.urls')),
]
```

- 개별 app

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('complete/', views.complete),
    
]
```



## 프로젝트 기본 설정(Templates 폴더 구조)

- 개별 app에 생성된 templates 폴더의 하위 디렉토리는 템플릿 파일로 활용된다.(기본설정)
- django는 템플릿 파일을 탐색하는 과정에서 DIRS와 INSTALLED_APPS 선언 순서에 따른다.
- 따라서, 다중 app으로 구성되는 경우 이름 중복이 발생가능하여 templates/{app이름}/{}.html으로 구조화한다.

- `APP_DIRS: True` app/templates/에 담아놓는다는 의미.




## form을 통한 요청 로직

**url을 다시 만들어야 함**

- 로그인 로직 하나

  - url/login

  - view def login

  - template.html

    <form action="login/">

- 처리 로직 하나

  - url/login/complete
  - view def complete



## Model

### 1. model 정의

```python
# django_crud/articles/models.py
class Article(model.Model):
    title = models.CharField(max_length=140)
    content=model.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
```

- `model.Model`을 상속받은 클래스를 생성한다.
- 속성은 내가 구성하고 싶은 테이블의 컬럼의 이름을 지정하고, 데이터 타입에 맞춰서 필드를 정의한다.

* `id` 필드는 자동적으로 `pk` 값으로 생성된다.

* 위에서 정의된 필드와 옵션 정보는 다음과 같다.

  * `CharField` :
    * `max_length` : 필수
  * `DateTimeField`
    * `auto_now_add` : (선택) 생성시에만 자동으로 해당 시간 값 설정
    * `auto_now` : (선택) 수정시마다 자동으로 해당 시간 값 설정
  * 이외의 필드는 https://docs.djangoproject.com/ko/2.1/ref/models/fields/#field-types 링크에서 확인

  

### 2. 마이그레이션

>  Migrations are Django’s way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema.

>  마이그레이션은 django에서 모델의 변경 사항을 데이터베이스 스키마에 반영하기 위한 방법이다.

- 정의된 모델을 데이터베이스에 반영하기 위해서는 마이그레이션 명령어를 통해 마이그레이션 파일을 생성한다.

  ```bash
  $ python manage.py makemigrations
  Migrations for 'articles':
    articles/migrations/0001_initial.py
      - Create model Article
  ```

- 마이그레이션 파일은 모델의 변경사항은 기록하며, app 별로 있는 `migrations/` 폴더에 기록된다. 최초에 `0001_initial.py` 라는 파일이 생성되어 있을 것이다.

- 생성된 마이그레이션 파일을 데이터베이스에 반영하기 위해서는 아래의 명령어를 입력한다.

  - 아래와 같이 많아 보이는 것은 django가 기본적으로 활용하고 있는 데이터베이스 마이그레이션 파일까지 반영되었기 때문이다. (앞으로는 프로젝트 생성과 동시에 `python manage.py migrate` 를 하자.)

```bash
$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, articles, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying articles.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying sessions.0001_initial... OK
```



## Django ORM

> 기본적인 데이터베이스 조작을 CRUD(Create, Read, Update, Delete) operation 이라고 한다.

### 0. django shell

>  python interactive interpreter를 django 프로젝트에 맞게 쓸 수 있는 기능

```bash
$ python manage.py shell
```

* 추가적인 패키지 설치를 통해 편하게 활용할 수 있다.

  ```bash
  $ pip install django-extensions ipython
  ```

  * `django-extensions` 는 django 개발에 있어서 유용한 기능들을 기본적으로 제공한다.
    * https://github.com/django-extensions/django-extensions
  * `ipython` 은 인터렉티브 쉘을 조금 더 편하게 활용하기 위해서 설치.

* 설치 이후에, `settings.py` 에 다음의 내용을 추가한다. (콤마 유의)

  ```python
  # django_crud/settings.py
  INSTALLED_APPS = [
      ...
      'django_extensions',
      'articles',
  ]
  ```

* 그리고 이제부터는 아래의 명령어를 사용한다.

  ```bash
  $ python manage.py shell_plus
  ```

* 쉘 종료 명령어는 `ctrl+d` 이다.



### 1. 생성

```python
article = Article()
article.title = '제목'
article.content = '내용'
article.save()
```



### 2. 조회

```python
Article.objects.all()
Article.objects.get(id=1)
```

* 전체 데이터 조회

  ```python
  Article.objects.all()
  >> <QuerySet [<Article: Article object (1)>]>
  ```

* 단일 데이터 조회

  > 단일 데이터 조회는 고유한 값인 id를 통해 가능하다.

  ```bash
  Article.objects.get(id=1)
  >> <Article: Article object (1)>
  ```

 

### 3. 수정

```pyhon
al = Article.objects.get(id=1)
a1.title = '제목 수정'
a1.save()
```

- 수정이 되었는지  확인하기 위해서 데이터 조회를 다시 해보자.

> 사용자가 입력한 내용으로 update하기 위해서는?
>
> **request.GET.get()**



### 4. 삭제

```python
a1 = Article.objects.get(id=1)
a1.delete()
>> (1, {'articles.Article': 1})
```



### ORM 장점

- SQL을 몰라도 DB 연동이 가능하다. (SQL 문법을 몰라도 쿼리를 조작할 수 있다.)
- SQL의 절차적인 접근이 아닌 객체 지향적인 접근으로 인해 생산성이 대폭 증가한다.
- ERD(DB 모델링 하는 것)를 보는 것에 대한 의존도를 낮출 수 있다.
- ORM은 해당 객체들을 재활용할 수 있다. 때문에 모델에서 가동된 데이터를 view와 template과 합쳐지는 형태로 MTV 디자인 패턴을 유지할 수 있다.



### ORM 단점

- ORM 만으로는 완전한 혹은 거대한 서비스를 구현하기는 어렵다.
- 사용이 쉬운 방면 설계는 신중하게 해야 한다.
- 오히려 프로젝트의 복잡성이 커질 경우 SQL보다 난이도가 상승할 수 있다.



## Admin 페이지 활용

### 1. 관리자 계정 생성

```bash
$ python manage.py createsuperuser
사용자 이름 (leave blank to use 'ubuntu'): admin1
이메일 주소:
Password:
Password (again):
Superuser created successfully.
```

### 2. admin 등록

> admin 페이지를 활용하기 위해서는 app 별로 있는 admin.py에 정의 되어야 한다.

```python
# django_crud/articles/admin.py
from django.contrib import admin

# Register your models here.
from .models import Article
admin.site.register(Article)
```

### 3. 확인

* `/admin/` url로 접속하여, 관리자 계정으로 로그인



---------

## 모델 작성 또는 변경 시 필수 3단계

1. models.py 작성
2. makemigrations
3. migrate



## **추가 명령어(옵션)**

sqlmigrate

python manage.py showmigrations : 설계도 확인


## 주의사항

- 관리자 계정은 반드시 migrate 이후에 진행해야 한다.

- 관리자 계정도 db에 저장할 곳이 있어야하기 때문에.

## 키워드
- ### Article.objects.all()
- ### Article(title=title, content=content)
- ### Article.objects.get(pk=1)