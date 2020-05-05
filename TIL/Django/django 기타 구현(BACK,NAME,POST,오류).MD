# 기본 CRUD 구현완료 후, 명세서 내의 BACK, NAME, POST, 오류 등 기타 구현

## BACK 추가

### new.html에 추가

```html
{% extends 'base.html' %}

{% block content %}
    <h1>NEW</h1>
    <form action="/articles/create/">
        <label for="title">TITLE:</label>
        <input type="text" id="title" name="title"><br>
        <label for="content">CONTENT</label>
        <textarea name="content" id="content" cols="30" rows="10"></textarea><br>
        <input type="submit" value="작성">
    </form>
    <a href="/articles/">BACK</a> #추가!
{% endblock %}
```

### detail.html에 추가

```html
{% extends 'base.html' %}
{% block content %}
    <h1>DETAIL</h1>
    <h2>{{ article.title }}</h2>
    <h3>{{ article.content }}</h3>
    <h3>작성일:{{ article.created_at }}</h3>
    <h3>수정일:{{ article.updated_at }}</h3>
    <a href="/articles/edit/{{ article.pk }}">EDIT</a>  <a href="/articles/delete/{{ article.pk }}">DELETE</a><br>
    <a href="/articles/">BACK</a> #추가!
{% endblock %}
```

### edit.html에 추가

```html
{% extends 'base.html' %}
{% block content %}
    <h1>EDIT</h1>
    <form action="/articles/update/{{ article.pk }}/">
        <label for="title">TITLE:</label>
        <input type="text" id="title" name="title" value="{{ article.title }}"><br>
        <label for="content">CONTENT:</label>
        <textarea name="content" id="content" cols="30" rows="10">{{ article.content }}</textarea><br>
        <input type="submit" value="수정">
    </form>
    <a href="/articles/detail/{{ article.pk }}">BACK</a>	#추가!
{% endblock %}
```





## name기능

1. urls.py에 appname과 url name 만들기.

   ```python
   from django.urls import path
   from . import views
   
   app_name = 'articles' #추가!
   
   urlpatterns = [
       path('', views.index, name='index'),
       path('new/', views.new, name='new'),
       path('create/', views.create, name='create'),
       path('edit/<int:pk>/', views.edit, name='edit'),
       path('detail/<int:pk>/', views.detail, name='detail'),
       path('update/<int:pk>/', views.update, name='update'),
       path('delete/<int:pk>/', views.delete, name='delete'),
   ]
   ```

2. 각 HTML 수정.

   1) index.html: 수정 전

   ```html
   {% extends 'base.html' %}
   
   {% block content %}
       <h1>INDEX</h1>
       <a href="new/">NEW</a>
       {% for article in articles %}
           <h2>제목: {{ article.title }}</h2>
           <h3>내용: {{ article.content }}</h3>
           <a href="/articles/detail/{{ article.pk }}">DETAIL</a>
           <hr>
       {% endfor %}
   {% endblock %}
   ```

   - index.html: 수정 후 ?? 무슨차이지;;

   ```html
   {% extends 'base.html' %}
   
   {% block content %}
       <h1>INDEX</h1>
       <a href="new/">NEW</a>
       {% for article in articles %}
           <h2>제목: {{ article.title }}</h2>
           <h3>내용: {{ article.content }}</h3>
           <a href="/articles/detail/{{ article.pk }}">DETAIL</a>
           <hr>
       {% endfor %}
   {% endblock %}
   ```

   2) new.html 수정 전

   ```html
   {% extends 'base.html' %}
   
   {% block content %}
       <h1>NEW</h1>
       <form action="/articles/create/">
           <label for="title">TITLE:</label>
           <input type="text" id="title" name="title"><br>
           <label for="content">CONTENT</label>
           <textarea name="content" id="content" cols="30" rows="10"></textarea><br>
           <input type="submit" value="작성">
       </form>
       <a href="/articles/">BACK</a>
   {% endblock %}
   ```

   수정 후

   ```html
   {% extends 'base.html' %}
   
   {% block content %}
       <h1>NEW</h1>
       <form action="{% url 'articles:create' %}">
           <label for="title">TITLE:</label>
           <input type="text" id="title" name="title"><br>
           <label for="content">CONTENT</label>
           <textarea name="content" id="content" cols="30" rows="10"></textarea><br>
           <input type="submit" value="작성">
       </form>
       <a href="{% url 'articles:index' %}">BACK</a>
   {% endblock %}
   ```

   

3) detail.html 수정 전

   ```html
   {% extends 'base.html' %}
   {% block content %}
       <h1>DETAIL</h1>
       <h2>{{ article.title }}</h2>
       <h3>{{ article.content }}</h3>
       <h3>작성일:{{ article.created_at }}</h3>
       <h3>수정일:{{ article.updated_at }}</h3>
       <a href="{/articles/edit/{{ article.pk }}">EDIT</a>  <a href="/articles/delete/{{ article.pk }}">DELETE</a><br>
       <a href="/articles/">BACK</a>
   {% endblock %}
   ```

   수정 후

   ```html
   {% extends 'base.html' %}
   {% block content %}
       <h1>DETAIL</h1>
       <h2>{{ article.title }}</h2>
       <h3>{{ article.content }}</h3>
       <h3>작성일:{{ article.created_at }}</h3>
       <h3>수정일:{{ article.updated_at }}</h3>
       <a href="{% url 'articles:edit' article.pk %}">EDIT</a>  <a href="{% url 'articles:delete' article.pk %}">DELETE</a><br>
       <a href="/articles/">BACK</a>
   {% endblock %}
   ```


  4) edit.html 수정 전

   ```html
   {% extends 'base.html' %}
   {% block content %}
       <h1>EDIT</h1>
       <form action="/articles/update/{{ article.pk }}/">
           <label for="title">TITLE:</label>
           <input type="text" id="title" name="title" value="{{ article.title }}"><br>
           <label for="content">CONTENT:</label>
           <textarea name="content" id="content" cols="30" rows="10">{{ article.content }}</textarea><br>
           <input type="submit" value="수정">
       </form>
       <a href="/articles/detail/{{ article.pk }}">BACK</a>
   {% endblock %}
   ```

   수정 후

   ```html
   {% extends 'base.html' %}
   {% block content %}
       <h1>EDIT</h1>
       <form action="{% url 'articles:update' article.pk %}/">
           <label for="title">TITLE:</label>
           <input type="text" id="title" name="title" value="{{ article.title }}"><br>
           <label for="content">CONTENT:</label>
           <textarea name="content" id="content" cols="30" rows="10">{{ article.content }}</textarea><br>
           <input type="submit" value="수정">
       </form>
       <a href="{% url 'articles:detail' article.pk %}">BACK</a>
   {% endblock %}
   ```

+  views의 redirect도  'app이름:url이름' 형식으로 수정하자!



## GET방식으로 POST 방식으로 변환.

form태그의 method의 default 값인 GET을 POST로 바꾼 후, request.GET -> request.POST 로 바꾼다.

이때 form 태그 밑에 {% csrf_token %}를 추가하는걸 잊지 말자.

1) edit.html수정전

```python
{% extends 'base.html' %}
{% block content %}
    <h1>EDIT</h1>
    <form action="{% url 'articles:update' article.pk %}/">
        <label for="title">TITLE:</label>
        <input type="text" id="title" name="title" value="{{ article.title }}"><br>
        <label for="content">CONTENT:</label>
        <textarea name="content" id="content" cols="30" rows="10">{{ article.content }}</textarea><br>
        <input type="submit" value="수정">
    </form>
    <a href="{% url 'articles:detail' article.pk %}">BACK</a>
{% endblock %}
```

수정 후

```python
{% extends 'base.html' %}
{% block content %}
    <h1>EDIT</h1>
    <form action="{% url 'articles:update' article.pk %}/" method="POST">
        {% csrf_token %}
        <label for="title">TITLE:</label>
        <input type="text" id="title" name="title" value="{{ article.title }}"><br>
        <label for="content">CONTENT:</label>
        <textarea name="content" id="content" cols="30" rows="10">{{ article.content }}</textarea><br>
        <input type="submit" value="수정">
    </form>
    <a href="{% url 'articles:detail' article.pk %}">BACK</a>
{% endblock %}
```

- views.py의 update도 수정.

```python
article.title = request.POST.get('title')
article.content = request.POST.get('content')
```

2) new.html 수정 전

```python
{% extends 'base.html' %}

{% block content %}
    <h1>NEW</h1>
    <form action="{% url 'articles:create' %}">
        <label for="title">TITLE:</label>
        <input type="text" id="title" name="title"><br>
        <label for="content">CONTENT</label>
        <textarea name="content" id="content" cols="30" rows="10"></textarea><br>
        <input type="submit" value="작성">
    </form>
    <a href="{% url 'articles:index' %}">BACK</a>
{% endblock %}
```

수정 후

```python
{% extends 'base.html' %}

{% block content %}
    <h1>NEW</h1>
    <form action="{% url 'articles:create' %}" method="POST">
        {% csrf_token %}
        <label for="title">TITLE:</label>
        <input type="text" id="title" name="title"><br>
        <label for="content">CONTENT</label>
        <textarea name="content" id="content" cols="30" rows="10"></textarea><br>
        <input type="submit" value="작성">
    </form>
    <a href="{% url 'articles:index' %}">BACK</a>
{% endblock %}
```

- views.py의 create도 수정

```python
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
```







## 오류 바꾸기 ??

views의 import에 `get_object_or_404` 추가

```python
from django.shortcuts import render, redirect, get_object_or_404
```

detail의 article 지정을 다음과 같이 변경

```python
#수정전
article = Article.objects.get(pk=pk)
#수정후
article = get_object_or_404(Article, pk=pk) 
```


![image-20200407005606242](C:\Users\a\Desktop\image-20200407005606242.png)![image](https://user-images.githubusercontent.com/60081212/78578383-6b487a80-786a-11ea-80d7-a525d26dba9d.png)

아직 저장하지 않은 pk값의 detail을 요청했을 때, 위의 오류 모습에서 아래와 같은 모습으로 바뀌게 된다.


![image](https://user-images.githubusercontent.com/60081212/78578583-b1054300-786a-11ea-8353-66ce657ed3b3.png)

![image](https://user-images.githubusercontent.com/60081212/78578319-4f44d900-786a-11ea-88e2-87704e4cdf8c.png)


