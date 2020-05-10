# HTTP 

## HTTP

- HyperText Transfer Protocol
- 리소스를 가져올 수 있도록 해주는 프로토콜, 웹에서 이루어지는 데이터 교환의 기초.
- 클라이언트-서버 프로토콜로 클라이언트에 의해 전송된 메시지는 요청(request), 서버에서 전송되는 메시지를 응답(response)



## 요청

- URL(Uniform Resource Locators)
  - 웹에서 정해진 유일한 자원의 주소

  `http://www.example.com:80/path/to/myfile.html?key1=value1&key2=value#Anchor`

  -> `프로토콜`://`도메인`:`포트`/`경로(path)`/?`파라미터`#`앵커`

- HTML에서 URL은 <a> : 링크, <link>/<script> : 문서의 연결, <img>/<video>/<audio> : 미디어, <iframe> 등에 사용된다.



## HTTP 요청 메시지

![image-20200407094000698](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20200407094000698.png)



## HTTP 메서드

- 주어진 리소스에 수행하길 원하는 행동으로 HTTP verb라고 부르기도 한다.
- `GET` : 특정 리소스의 표시
  - <a> 태그 <form> 및 브라우저에서 주소창을 보내는 요청 등
  - url을 활용(쿼리스트링)하여 데이터를 전송함 따라서, 크기 제안 및 보안 이슈가 있음
  - 서버로부터 정보를 조회하기 위한 http 메서드
  - 데이터 크기에 제한이 있다.
- `POST`: 특정 리소스에 제출(서버의 상태 변화).
  - 보통 HTML Form을 통해 서버에 전송하며, 서버의 변경사항을 만듦.
  - HTTP 요청 메시지의 body에 데이터를 전송함. 따라서 길이의 제한 없이 데이터 전송 가능
  - 서버에서 리소스를 생성, 수정, 삭제 등 변경하기 위한 http 메서드
  - url에 안보인다고해서 안전하다고 생각될 수 있지만, 개발자도구나 다른 개발 툴을 이용하면 확인이 가능. 반드시 민감한 정보에 경우 암호화해서 전송해야 함.
  - 게시판 글 작성, 사용자 추가, 회원가입



## HTTP 응답 메시지

![image-20200407094459166](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20200407094459166.png)



## HTTP 상태코드

![image-20200407094548317](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20200407094548317.png)



# 

---------

### index 목록 최신순 

- views.py

  ```python
  def index(request):
      articles = Article.objects.order_by('-pk')
      context = {
          'articles': articles,
      }
      return render(request, 'articles/index.html', context)
  ```



### 새로운 form 방식

- urls.py

  ```python
  from django.urls import path
  from . import views
  
  app_name = 'articles'
  
  urlpatterns = [  
    path('new/', views.new, name='new'),
  ]
  ```

- forms.py 

  ```python
  from django import forms
  
  class ArticleForm(forms.Form):
      title = forms.CharField(max_length=30)
      content = forms.CharField(widget=forms.Textarea)
      ##### 근데 이거 models.py와 너무 중복이다 그래서 연동해줄래~
      
  from django import forms
  from .models import Article # 모델에서 클래스 들고옴
  
  class ArticleForm(forms.ModelForm): # 모델의 폼
      class Meta:
          model = Article
          fields = ['title', 'content'] # 모델에서 필드 들고옴
  ```

- views.py

  ```python
  from django.shortcuts import render, redirect
  from .models import Article
  from .forms import ArticleForm
  
  def new(request):
      form = ArticleForm()
      context = {
          'form': form
      }
      return render(request, 'articles/new.html', context)
  ```

- new.html

  ```html
  {% extends 'base.html' %}
  
  {% block content %}
  <h1>NEW</h1>
  <hr>
  <form action="" method="post">
      {% csrf_token %}
      {{ form.as_p }}
      <input type="submit" value="전송">
  </form>
  <a href="{% url 'articles:index' %}">BACK</a>
  {% endblock %}
  ```



### 마지막에 한 NEW + CREATE 하는방식

- views.py

  ```python
  from django.shortcuts import render, redirect
  from .models import Article
  from .forms import ArticleForm
  
  def new(request):
      if request.method == 'POST':
          # POST /articles/new/ => (구) create 함수
          form = ArticleForm(request.POST)
          if form.is_valid():
              article = form.save()
              return redirect('articles:index')
  
      else:
          # GET /articles/new/
          form = ArticleForm()
      # 공용 context
      context = {
          'form': form
      }
      return render(request, 'articles/new.html', context)
  ```

  - 흐름 :  처음에 GET 으로 article/new/를 연다(?) -> else문이 실행 -> POST 로 form을 받아온다 -> if문 실행 -> 값이 유효하면 if 문 안의 if 문이 실행된다 -> 저장하고, redirect가 이루어진다



## ModelForm 장점

- input 태그에 대한 httml 옵션들을 자동으로 설정해준다.
- 데이터에 대한 유효성 검사를 실시할 수 있다.
- 입력된 값이 유효하지 않은 경우 에러페이지를 띄우는게 아니라 에러 메세지가 포함된 form을 출력해준다.





