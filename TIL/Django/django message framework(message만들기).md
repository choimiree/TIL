# django message framework

> flash message(one time notification message)



# message 만들기

- `from django.contrib import messages` 로 불러와야 사용 가능

> 앱이름: artcles

## views.py

```python
from django.contrib import messages


def index(request):
    articles = Article.objects.order_by('-pk')	#최신순으로 보여지는 것
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
        messages.warning(request, '폼을 다시 확인 후 제출해주세요.')
    else:
        form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'articles/forms.html', context)

```

## settings.py

- `settings.py`에서 TEMPLATES에 `DIRS: [os.path.join(BASE_DIR, 'templates')` 설정 추가 하기
- `MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'` 마지막에 추가해주면 c9, redirect 메세지 프레임워크 사용 가능!
- bootstrap css, js 복사해서 붙이기

## templates/base.html

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
    {% if messages %}
    <ul class="messages">
        {% for message in messages %}
        <li>{% if message.tags %} class="{{ message.tags }}"{% endif %}>{{ message }}</li>
        {% endfor %}
    </ul>
    {% endif %}
    {% block content %}
    {% endblock %}
    <a href="{% url 'articles:index' %}">목록</a>
</body>
</html>
```

## articles/templates/index.html

```html
{% extends 'base.html' %}

{% block title %} 목록 {% endblock %}

{% block content%}
    {% for article in articles %}
        <p>{{ article.pk }}</p>
		<a href="{% url 'articles:detail' article.pk %}">글 보러가기</a>
		<hr>
    {% endfor %}
{% endblock %}
```

## articles/templates/forms.html

```html
{% extends 'base.html' %}

{% block title %} 새 글쓰기 {% endblock %}

{% block content%}
    <form action="" method="POST">
        {% csfr_token %}
        {{ form.as_p }}
        <button>작성</button>
	</form>
{% endblock %}
```

## articles/templates/detail.html

```html
{% extends 'base.html' %}

{% block title %}{{ article.pk }}번 글{% endblock %}

{% block content%}
<h1>{{ article.pk}}: {{ article.title }}</h1>
<p>{{ article.content }}</p>
{% endblock %}
```

