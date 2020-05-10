# Django 일기: 사용자 인증관리

오늘은 Django 사용자 인증관리에 대해 공부했다. 이를 활용해 instagram 클론 코딩을 할 수 있다. 사용자 인증관리란 회원가입, 로그인 form을 만드는 것이다. 맛보기로 보여드리자면, 아래와 같은 것이다.

```python
def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if for.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
         'form': form
     }
    return render(request, 'accounts/form.html', context)
```



그럼 바로 프로젝트를 실행하고 **accounts** 앱을 만들어 **회원가입** 페이지를 만들어보자.



## 1. 프로젝트 생성(프로젝트명: choistagram)

```bash
$django-admin startproject choistagram
```

인스타그램 클론코딩을 할거니까 프로젝트명은 choistagram으로 명명했다ㅎㅎ 

## 2. 앱 만들기(accounts)

```bash
$python manage.py startapp accounts
```

### settings.py 기본 설정

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
ALLOWED_HOSTS = ['*']
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
```

project를 만들고 manage.py와 같은 위치에서 app도 만들어준다. 그리고 프로젝트 기본 세팅에 앱을 추가하고 위와 같이 변경해준다.

> naming 설정 시: 앱은 복수형, 모델은 단수형



회원가입은 하나의 어떤 User를 만드는 것이다. 이는 CRUD로직 중 Create을 구현하는 것과 동일하다. django에서는 user model(이름,아이디,비밀번호 등)과 model form이 이미 구현되어 있기 때문에, User Class를 끌어와서 import만 해주면 된다. 기본 골자는 model form기반의 create함수에 대한 코드를 따른다. 아무튼 model 설정을 따로 안해줘도 되고 migrate만 해준다.

> (참고) User objects 관련 공식문서: https://docs.djangoproject.com/en/3.0/topics/auth/default/

## 3. models.py

```bash
$python manage.py migrate
```

model에선 이것만 해주면 된다. 바로 프로젝트 urls.py로 간다.

## 4. 프로젝트/urls.py

```python
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
]
```

## 5. 앱/urls.py 생성

```python
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
]
```

urls설정이 끝나면 views.py로 가서 `django.contrib.auth.form` 내 구현되어있는 회원가입 model form인 `UserCreationForm`을  import해준다.

## 6. views.py

```python
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    signup_form = UserCreationForm()
    context = {
        'signup_form': signup_form
    }
    return render(request, 'accounts/signup.html', context)
```

일단 논리에 따라 기본적인 것만 설정한 다음 흘러가보자. 다음으로 signup.html 생성해서 일단 잘 만들어진지 서버를 돌려 확인해볼 예정이다. 

## 6-1. views.py 추가

서버를 돌려 확인해본 뒤(7번 실행) 다시 돌아와서 views.py를 추가해준다.

```python
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    #HTTP method가 POST인 경우
    if request.method == 'POST':
        signup_form = UserCreationForm(request.POST)
        #form의 유효성 검증이 valid할 경우, DB에 저장
        if signup_form.is_valid():
            signup_form.save()
            #게시글 목록 페이지
        return redirect('articles:index')
    #HTTP method가 GET인 경우
    else:
        signup_form = UserCreationForm()
    context = {
        'signup_form': signup_form
    }
    return render(request, 'accounts/signup.html', context)
```



## 7. signup.html 생성

```html
{% extends 'base.html' %}

{% block body %}
	<form action="" method="POST">
        {% csrf_token %}
        {{ signup_form.as_p }}
        <button>
            회원가입 신청
        </button>
</form>
{% endblock %}
```

signup.html 생성하기 전에 base.html이 프로젝트와 앱폴더와 동일한 위치에 생성돼있어야 한다.

### base.html

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Instagram - {% block title %}{% endblock %}</title>
    {% block css %}
    {% endblock %}
</head>
<body>
    {% block body %}
    {% endblock %}
</body>
</html>
```

언어를 한국어로 바꾸고`"ko"` 기본 설정만 해준 것이다. base.html 설정 후에는 settings.py의 TEMPLATES에 `DIRS: [os.path.join(BASE_DIR, 'templates')]` 설정을 추가해준다. 



이쯤에서 서버돌려서 잘 뜨는지 확인을 해준다.

```bash
$python manage.py runserver 8080
```

![image-20200414081128706](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20200414081128706.png)

잘 뜨는 걸 확인할 수 있었다!  6-1번으로 돌아가서 views.py를 보완해주자.

이후 urls.py, views.py, 앱/templates/html을 반복해가며 추가해주면 된다. 

나는 signup을 만들었으니 index페이지, detail페이지와 update페이지를 만들러 가봐야겠다. 오늘의 일기 끄읕!