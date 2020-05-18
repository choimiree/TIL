# django 처음부터~

## 1. 프로젝트 만들기

```bash
$django-admin startproject crud
```

## 2. 앱 만들기

```bash
$python manage.py startapp articles
$python manage.py startapp accounts
```

## 3. settings.py 앱 추가

```python
ALLOWED_HOSTS = ['*']
INSTALLED_APPS=[
    'articles',
    'accounts',
]
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
```

## 4. server 확인

```bash
$ python manage.py runserver 8080
```

## 5. articles 앱 model설정

```python
from django.db import models
from django.conf import settings

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=30)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Comments(models.Model):
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    article=models.ForeignKey(Article, on_delete=models.CASCADE)
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)



```

## 6. accounts 앱 model 설정

```python
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass
```

:heavy_check_mark: accounts 모델 쓸 때,  `AbstractBaseUser`말고 `AbstractUser` 모델 쓰는 이유는?

:arrow_right: 자유도가 높아서.

### settings.py에 User 모델 추가

```python
AUTH_USER_MODEL = 'accounts.User'
```

- articles앱 모델에 user정보 가져와서 article:user=1:N관계 만들어준다.

- comment는 article과 1:N관계. 
- comment는 user랑도 1:N관계

### migrate

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

:heavy_check_mark: **역참조**: 1이 N을 참조하는 것. 

article 입장에서 모든 comment를 가져오는 것은 'article.comment_set'

user입장에서 모든 comment를 가져오는 것은 'user.comment_set'

겹치는 거 아닌데 왜 사용?? 

user.article_set이 있는데 ''좋아요''하면, user.article_set(many to many field) 생김. 그러면 겹치기 때문에 'related_name'사용.

## 7. admin 관리자 생성

```bash
$ python manage.py createsuperuser
```

### articles/admin.py 등록

```python
from django.contrib import admin
from .models import Article, Comments


admin.site.register(Article)
admin.site.register(Comments)

```

### accounts/admin.py 등록

```python
from django.contrib import admin
from .models import User


admin.site.register(User)
```

- admin server에서 작성/수정/삭제 잘 되는지 확인
- 출력되는 무언가가 있어야하기 때문에 하나 작성해놓는다.

## 8. forms.py

```python
from django import forms
from .models import Article, Comments

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = '__all__'
```

## 9. 프로젝트/urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
]
```

## 10. articles: read

### urls.py

```python
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
 path('', views.index, name='index'),   
]
```

- 요청이 가장 먼저 도착하는 곳이 **url**이기 때문에 제일 먼저 짠다.

### views.py

```python
from django.shortcuts import render
from .models import Article

'''
1. class based-views - cbv
2. function based-views - fbv: 로직 숙지하면 cbv로, 근데 cbv가 짱인건 아님. 개발이 빠르고 해주는게 많지만, 그 반대로 우리가 커스텀할게 별로 없음. 자유도가 떨어짐. fbv는 우리가 커스텀을 자유롭게 할 수 있음.
'''

def index(request):
    articles = Article.objects.all()
    context = {
        #'articles'가 html로 넘어가는 거.
        'articles': articles,
        
    }
    return render(request, 'articles/index.html', context) #templates 폴더 이후에라서 앞에 templates/ 생략해도 된다.

```

## 11. articles에 templates 폴더 생성 

- articles/templates/articles/index.html

  (이렇게 한 개 더 안만들어주면 index가 가장 위에꺼로 감(?))

### index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>
        INDEX
    </h1>
    <hr>
    {% for article in articles %}
    <h3>
        {{ article.title }}
    </h3>
    {% endfor %}
</body>
</html>
```

-------------------

:memo: import하는거 안외워도 된다고 하셨는데, account model짤때 AbstratUser 모델 import 어디참고해서 가져오셨죠?

:memo: class Meta 왜 쓴다고 하셨죠?



## 12. base.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <title>Document</title>
</head>
<body>
    {% block content %}
    {% endblock %}
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
</body>
</html>
```



:memo: 기본 템플릿 경로 로직:

`app폴더/templates/....경로...`

```python
#settings.py
DIRS : [os.path.join(BASE_DIR, 'templates')]
```

​	:arrow_right: 이거 안하면 `Template error` 뜸



:heavy_check_mark:base directory의 이름은 바꿔도 된다!



## 13. articles: create

### urls.py

article `조회(R)`했으니까, `작성(C)`해야하므로 `urls.py`로 고고

```python
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
]
```

### views.py

- **POST**: db에 작성되도록 하는 것
- **GET**: db가 작성되는 html 파일을 rendering

```python
from django.shortcuts import render
from .models import Article

def create(request):
    if request.method == 'POST':
        pass
    else:
        article_form = ArticleForm()
    context = {
        'article_form': article_form,
    }
    return render(request, 'articles/create.html', context)
```

### index.html

```html
{% extends 'base.html' %}
{% block content %}
<h1>INDEX</h1>
<a href="{% %}">CREATE</a>
<hr>
{% for article in articles %}
    <h3>{{ article.title }}</h3>
    <h4>
        작성자: {{ article.user }}
    </h4>
{% endfor %}
{% endblock %}
```

:heavy_check_mark: {% %} 안에 `url template tag` 쓰면된다.

```html
{% extends 'base.html' %}
{% block content %}
<h1>INDEX</h1>
<a href="{% url 'articles:create' %}">CREATE</a>
<hr>
{% for article in articles %}
    <h3>{{ article.title }}</h3>
    <h4>
        작성자: {{ article.user }}
    </h4>
{% endfor %}
{% endblock %}
```

### create.html

```html
{% extends 'base.html' %}
{% block content %}
<h1>CREATE</h1>
<form action="" method="POST">
    {% csrf_token %}
    {{ article_form.as_p }}
    <button>
        CREATE
    </button>
</form>
{% endblock %}
```

서버 돌려 보면 불필요한 `user` 옵션이 있다. 어떻게할 것 인가?

![image-20200512185306438](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20200512185306438.png)

`forms.py`에서 `fields` 조정하면 된다. 제외하는게 편하면 제외하는 걸로.

### forms.py

```python
from django import forms
from .models import Article, Comments


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        # fields = '__all__'
        fields = ['title', 'content',]


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = '__all__'
```

이제 `views.py`의 POST 부분 작성

### views.py

```python
from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save(commit=False)
            return redirect('articles:index')
    else:
        article_form = ArticleForm()
    context = {
        'article_form': article_form,
    }
    return render(request, 'articles/create.html', context)
```

:heavy_check_mark:`commit=False` 안하면 `Integrity Error`.

![image-20200512185854818](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20200512185854818.png)

해당게시글의 실제 db의 `articles_article`(테이블)에 `user_id`가 `NULL`이 안된다는 말. instance를 통해 custom해주라고 해야됨.

`commit=False` -> 저장하진 않고 return값(article)만 준다. 객체는 만들고 저장은 하지 말라는 말.

`article.user`에 `request.user.pk` 넣어줘야함.

```python
from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form = article_form.save(commit=False)
            article_form.user = request.user
            article_form.save()
            return redirect('articles:index')
    else:
        article_form = ArticleForm()
    context = {
        'article_form': article_form,
    }
    return render(request, 'articles/create.html', context)
```

request안에 user의 정보가 있기 때문에, article에 user정보를 넣고, 돌아가도록 해야함.



## 14. articles: detail

### urls.py

```python
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/', views.detail, name='detail'),

    ]
```

### views.py

```python
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)
```

### detail.html

```html
{% extends 'base.html' %}
{% block content %}
<h1>DETAIL</h1>
<h2>{{ article.title }}</h2>
<h2>{{ article.content }}</h2>
<a href="{% url 'articles:index' %}">back</a>
{% endblock %}
```

### index.html

detail.html로 연결되는 링크 추가

```html
{% extends 'base.html' %}
{% block content %}
<h1>INDEX</h1>
<a href="{% url 'articles:create' %}">CREATE</a>
<hr>
{% for article in articles %}
    <h3>{{ article.title }}</h3>
    <h4>
        작성자: {{ article.user }}
    </h4>
    <a href="{% url 'articles:detail' article.pk %}">DETAIL</a>
    <hr>
{% endfor %}
{% endblock %}
```

article_pk가 아니라 article.pk! 왜인지 알지?

## 15. articles: update

### urls.py

```python
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),   #GET, POST
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:article_pk>/update/', views.update, name='update'),  #GET, POST
    ]
```

### views.py

일단 POST부분은 pass 하고, form을 보여줘야 한다. 하지만 이렇게만 하면 문제발생! **수정해야할 게시글**이 있어야함! `article=get_object_or_404` 가져와야함. `ArticleForm()`에 `(instance=article)` 필수는 아니지만 넣어도 됨. 왜냐? 기존에 저장됐던 게시글을 가져와야하기 때문에. 기존의 글이 없으면 create form이 나옴.

```python
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        pass
    else:
        article_form = ArticleForm()
    context = {
        'article_form': article_form,
    }
    return render(request, 'articles/update.html', context)
```

### update.html

```html
{% extends 'base.html' %}
{% block content %}
<h1>UPDATE</h1>
<form action="" method="POST">
    {% csrf_token %}
    {{ article_form.as_p }}
    <button>UPDATE</button>
</form>
{% endblock %}
```

### detail.html

update.html로 갈 수 있게 링크 추가

```html
{% extends 'base.html' %}
{% block content %}
<h1>DETAIL</h1>
<h2>{{ article.title }}</h2>
<h2>{{ article.content }}</h2>
<a href="{% url 'articles:index' %}">back</a>
<a href="{% url 'articles:update' article.pk %}">UPDATE</a>
{% endblock %}
```

### views.py

이제 pass한 부분 보완.

ArticleForm()은 수정이 되려면, 무엇이 필요? 새로보낸 데이터 필요! POST안에 데이터있다. (`request.POST, instance=article`) 기존 데이터로 먼저 수정할 수 있는 폼을 만들고, 수정된 폼은 새로운 요청으로 만든다.

```python
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        #Create a form to edit and existing Article,
        #but use POST data to populate the form
        article_form = ArticleForm(request.POST, instance=article)
    else:
        article_form = ArticleForm()
    context = {
        'article_form': article_form,
    }
    return render(request, 'articles/update.html', context)
```

수정할 객체 만들어졌으면 유효성 검증 후 저장.

이미 user 정보가 있어서, commit=False는 안한다. update라는 동작 자체는 title, content만 덮어씌우면 되는거지, user 정보는 덮어씌우면 안된다.

```python
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        #Create a form to edit and existing Article,
        #but use POST data to populate the form
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:detail', article.pk)
    else:
        article_form = ArticleForm()
    context = {
        'article_form': article_form,
    }
    return render(request, 'articles/update.html', context)
```

유효성에서 튕겨져 나오면, else의 context로 간다. 왜 통과되지 않았는지 에러메시지를 자연스럽게 가지고 나간다!! 따라서, error message를 따로 설정하지 않아도 되는 것.

## 16. articles: delete

### urls.py

```python
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),   #GET, POST
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:article_pk>/update/', views.update, name='update'),  #GET, POST
    path('<int:article_pk>/delete/', views.delete, name='delete'),
    ]
```

### views.py

```python
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return redirect('articles:index')
```

### detail.html

```html
{% extends 'base.html' %}
{% block content %}
<h1>DETAIL</h1>
<h2>{{ article.title }}</h2>
<h2>{{ article.content }}</h2>
<a href="{% url 'articles:index' %}">back</a>
<a href="{% url 'articles:update' article.pk %}">UPDATE</a>
<a href="{% url 'articles:delete' article.pk %}">DELETE</a>
{% endblock %}
```

a태그는 get방식! 따라서 form 태그가 필요함

```html
{% extends 'base.html' %}
{% block content %}
<h1>DETAIL</h1>
<h2>{{ article.title }}</h2>
<h2>{{ article.content }}</h2>
<a href="{% url 'articles:index' %}">back</a>
<a href="{% url 'articles:update' article.pk %}">UPDATE</a>
<a href="{% url 'articles:delete' article.pk %}">DELETE</a>
<form action="{% url 'articles:delete' article.pk %}" method="POST">
    {% csrf_token %}
    <button>DELETE</button>
</form>
{% endblock %}
```

:heavy_check_mark: POST일때만 삭제하게(GET방식일 때 삭제할 수 있게하면, url만 조작해서 삭제할 수 있으니까 막는것!) GET은 조회밖에 못한다고 생각하면 됨!

#### decorator

delete도 POST형식으로 받아야함!

```python
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm


@require_POST
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return redirect('articles:index')
```



## :heavy_plus_sign: 댓글

### urls.py

```python
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),   #GET, POST
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:article_pk>/update/', views.update, name='update'),  #GET, POST
    path('<int:article_pk>/delete/', views.delete, name='delete'),
    path('<int:article_pk>/comments/', views.comments_create, name='comments_create'),
    ]
```

### views.py

```python
from ~ require_POST
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm, CommentForm


def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment_form = CommentForm()
    #article이 가지고 있는 댓글을 다 가져오는 것
    comments = article.comments_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)

@require_POST
def comments_create(request, article_pk):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        #실제 table의 colum명을 써야하기 때문에 article_id를 써야한다.
        comment.article_id = article_pk
        comment.save()
    return redirect('articles:detail', article_pk)
```

### forms.py

```python
from django import forms
from .models import Article, Comments


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        # fields = '__all__'
        fields = ['title', 'content',]


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ['content']
```

### detail.html

```html
{% extends 'base.html' %}
{% block content %}
<h1>DETAIL</h1>
<h2>{{ article.title }}</h2>
<h2>{{ article.content }}</h2>
<a href="{% url 'articles:index' %}">back</a>
<a href="{% url 'articles:update' article.pk %}">UPDATE</a>
<a href="{% url 'articles:delete' article.pk %}">DELETE</a>
<form action="{% url 'articles:delete' article.pk %}" method="POST">
    {% csrf_token %}
    <button>DELETE</button>
</form>
<hr>
<h3>댓글 목록</h3>
{% for comment in comments %}
	<p>{{ comment.user }}: {{ comment.content }}</p>
{% endfor %}
<hr>

<h3>댓글작성</h3>
<form action="{% url 'articles:comments_create' article.pk %}" method = "POST">
    {% csrf_token %}
    {{ comment_form.as_p }}
    <button>댓글 작성</button>
</form>
{% endblock %}
```



>  USER CRUD 시작

:star: accounts 계정이 어렵게 느껴지는 이유: user가 본인이 맞는지, 로그인된 user가 맞는지 등등 자잘자잘한게 많아서 어려워보이는 것.



## 17. accounts: 회원가입

### project/urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('accounts/', include('accounts.urls')),
]
```

:heavy_check_mark: user에 관한 앱은 왜 `accounts`로 설정하면 좋다고 했게?

decorator에 `login_required` 기억남? 그거 문서 잘 읽어보면 ![image-20200512194047314](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20200512194047314.png)

장고에 auth에 관한 기본값을 accounts로 쓰고 있다. 만약 accounts를 안 쓴다면, 서로 매칭이 안돼서 신경쓸게 많아짐. 그래서 accounts가 아니라 ssafy라고 쓰면 settings에

```python
#settings.py
LOGIN_URL = '/ssafy/signin/'
```

이렇게 추가로 적어줘야 됨.

### accounts/urls.py

```python
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),

    ]
```

### views.py

```python
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup(request):    #CREATE
    if request.method == 'POST':
        pass
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


```

### signup.html

```html
{% extends 'base.html' %}

{% block content %}
<h1>SIGN UP</h1>
<form action="" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button>회원가입</button>
</form>
{% endblock %}
```

### base.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <title>Document</title>
</head>
<body>
    <div class='container'>
        <a href="{% url 'accounts:signup' %}">회원가입</a>
    </div>
        {% block content %}
        {% endblock %}
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
</body>
</html>
```

이제 회원가입 눌렀을 때 이뤄지는 코드를 `views.py`에 넣어야한다: `form`이 필요할것! form하고 `유효성검증` 후 `저장`

```python
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup(request):    #CREATE
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)
```

이렇게 하면 `AttributeError` 뜸

![image-20200512195341238](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20200512195341238.png)

:heavy_check_mark: `modelform`은 Meta정보가 꼭 있다는 말. meta 정보 보면 auth = User에서 User가 가리키는 것이 우리가 설정한 User랑 다르기 때문에, modelform에서 User를 고쳐줘야한다.

:heavy_plus_sign: 안바꿔줘도 되는 `form`

![image-20200512195839497](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20200512195839497.png)

이건 modelform이 아니라 form으로 만들어졌기때문에 안바꿔줘도 된다.

modelform은 우리가 커스텀한걸로 바꿔줘야한다.

![image-20200512195914183](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20200512195914183.png)

### accounts/forms.py

일단 기본적으로 만들어져있는 `UserCreationForm`을 상속받아서 수정.

우리는 User 가져올때 `get_user_model()` 형식으로 가져왔다.

```python
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields
```

기존 UserCreationForm에서 model만 바꿨음.

CustomUserCreationForm을 `views.py`에 가져옴

### views.py

```python
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm

# Create your views here.
def signup(request):    #CREATE
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)
```



## 18. accounts: 로그인

### accounts/urls.py

```python
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),

    ]
```

### views.py

```python
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import get_user_model()
from .forms import CustomUserCreationForm

def login(request):	#CREATE(user session)
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)	#form은 request.POST형태로
        if form.is_valid():
            #세션생성:login
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/login.html', context)
```

```


```

### login.html

```html
{% extends 'base.html' %}

{% block content %}
<h1>LOGIN</h1>
<form action="" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button>로그인</button>
</form>
{% endblock %}
```

### base.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <title>Document</title>
</head>
<body>
    <div class='container'>
        <a href="{% url 'accounts:signup' %}">회원가입</a>
        <a href="{% url 'accounts:login' %}">로그인</a>
    </div>
        {% block content %}
        {% endblock %}
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
</body>
</html>
```

## 19. accounts: 로그아웃

### accounts/urls.py

```python
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    ]
```

### views.py

```python
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
#from django.contrib.auth import get_user_model()
from .forms import CustomUserCreationForm

# Create your views here.
def signup(request):    #CREATE
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def login(request):	#CREATE(user session)
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)	#form은 request.POST형태로
        if form.is_valid():
            #세션생성:login
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/login.html', context)


def logout(request):	#DELETE(user session)
    auth_logout(request)
    return redirect('articles:index')
```

### base.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <title>Document</title>
</head>
<body>
    <div class='container'>
        <a href="{% url 'accounts:signup' %}">회원가입</a>
        <a href="{% url 'accounts:login' %}">로그인</a>
        <a href="{% url 'accounts:logout' %}">로그아웃</a>
    </div>
        {% block content %}
        {% endblock %}
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
</body>
</html>
```

### :heavy_plus_sign: 접근 제한

#### `is_authenticated` attribute 사용

#### base.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <title>Document</title>
</head>
<body>
    <div class='container'>
        {% if user.is_authenticated %}
            <h1>{{user.username}}님, 안녕하세요!</h1>
        	<a href="{% url 'accounts:logout' %}">로그아웃</a>
        {% else %}
        	<a href="{% url 'accounts:signup' %}">회원가입</a>
        	<a href="{% url 'accounts:login' %}">로그인</a>
		{% endif %}
        {% block content %}
        {% endblock %}
    </div>

    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
</body>
</html>
```

#### views.py

```python
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
#from django.contrib.auth import get_user_model()
from .forms import CustomUserCreationForm

# Create your views here.
def signup(request):    #CREATE
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def login(request):	#CREATE(user session)
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)	#form은 request.POST형태로
        if form.is_valid():
            #세션생성:login
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/login.html', context)


def logout(request):	#DELETE(user session)
    auth_logout(request)
    return redirect('articles:index')
```

### :heavy_plus_sign: 자동 로그인

회원가입을 했다고 해서 로그인이 되는게 아니다

#### views.py

```python
def signup(request):    #CREATE
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)	#modelform은 정보만
        if form.is_valid():
            user = form.save()
            #print(form.save()): user정보가 생긴걸 확인할 수 있다.
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

def login(request):	#CREATE(user session)
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)	#form은 request.POST형태로
        if form.is_valid():
            #세션생성:login
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request):	#DELETE(user session)
    auth_logout(request)
    return redirect('articles:index')
    
```

### :heavy_plus_sign: 인증된 사용자만 작성/수정/삭제할 수 있게

#### index.html

```html
{% extends 'base.html' %}
{% block content %}
<h1>INDEX</h1>
{% if user.is_authenticated %}
	<a href="{% url 'articles:create' %}">CREATE</a>
<hr>
{% else %}
	<a href="{% url 'accounts:login' %}">글을 작성하려면 로그인하시오.</a>
{% endif %}
<hr>
{% for article in articles %}
    <h3>{{ article.title }}</h3>
    <h4>
        작성자: {{ article.user }}
    </h4>
{% endfor %}
{% endblock %}
```

#### `login_required()` decorator 사용

#### create/detail/delete views.py

```python
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Article, Comments
from .forms import ArticleForm, CommentForm

@login_required
def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save(commit=False)
            return redirect('articles:index')
    else:
        article_form = ArticleForm()
    context = {
        'article_form': article_form,
    }
    return render(request, 'articles/create.html', context)

@login_required
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        pass
    else:
        article_form = ArticleForm()
    context = {
        'article_form': article_form,
    }
    return render(request, 'articles/update.html', context)

#@login_required
@require_POST
def delete(request, article_pk):
    if user.is_authenticated:
	    article = get_object_or_404(Article, pk=article_pk)
    	article.delete()
    return redirect('articles:index')
```

:heavy_check_mark: `is_authenticated`와 `login_required()`의 차이

`is_authenticated`는 next 처리를 할 수 없고, 어디론가 되돌리는 것만 가능하다.

:heavy_check_mark: @login_required 랑 @require_POST 같이 쓸 수 없는 이유!

**비로그인 상태 DELETE  요청(POST) **

**-> 로그인 검증(@login_required) **

**-> 로그인 페이지로 리다이렉트(next='/articles/delete/') **

**-> 로그인 성공 **

**-> next 주소로 redirect (GET)**

**-> GET요청으로 next 파라미터 처리 **

**-> @required_POST **

**-> 405 Method Not Allowed**



#### login_views.py

```python
def login(request):	#CREATE(user session)
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)	#form은 request.POST형태로
        if form.is_valid():
            #세션생성:login
            auth_login(request, form.get_user())
            #print(request.GET)
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/login.html', context)
```

