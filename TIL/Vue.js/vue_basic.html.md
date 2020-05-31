# vue_basic.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <!-- View -->
  <div id="app">
    {{ message }} - {{ count }}
    <button v-on:click="plus">plus</button>
    <button v-on:click="minus">minus</button>
  </div>

  <!-- 1. vue CDN 추가 -->
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <!-- ViewModel -->
  <script>
    // 2. 모든 Vue앱은 Vue class로부터 새로운 인스턴스를 만드는 것부터 시작
    const app = new Vue({
      // 인스턴스의 속성
      el: '#app',
      data: {
        message: 'Hello, vue !',
        count: 0,
      },
      methods: {
        // 표현식
        plus: function () {
          console.log(this)
          this.count++
        },
        // 선언식
        minus() {
          console.log(this)
          this.count--
        }
      }
    })
  </script>
</body>
</html>

```



# vue의 핵심

## 우리는 Vue instance로 DOM을 조작한다.

## html element(View)는 Vue를 위한 껍데기 역할이다.

## 중심은 모두 Vue instance 안에 있다.



# vue_directive.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <div id="app">
    <!-- v-text -->
    <!-- 둘 다 같은 코드 -->
    <p>{{ name }}</p>
    <p v-text="name"></p>

    <!-- v-html -->
    <!-- 문자열 html을 실제 html 형태로 렌더링 해준다.-->
    <p>{{ message }}</p>
    <p v-html="message"></p>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        name: 'marry',
        message: '<h1>h1 태그입니다.</h1>'
      }
    })
  </script>
</body>
</html>

```

# if_vs_show.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <div id="app">
    <!-- 조건에 맞지 않으면 렌더링 자체를 하지 않음. -->
    <p v-if="false">{{ name }}</p>
    <!-- 조건과 관계없이 일단 렌더링 후에, 조건에 맞지 않으면 CSS display 속성을 none으로 숨겨버림. -->
    <p v-show="false">{{ name }}</p>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        name: 'happy'
      }
    });
  </script>
</body>
</html>

```

# get_cat_image.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    img {
      display: block;
      width: 300px;
      height: 300px;
    }
  </style>
</head>
<body>
  <h1>Cat Image</h1>
  <div id="cat">
    <button v-on:click="getCatImg">고양이 이미지 바꾸기</button>
    <div v-if="catImages.length">
      <img v-for="(image, index) in catImages" :key="index" v-bind:src="image" alt="cat-img">
    </div>
    <p v-else>No Image</p>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    // case 1
    const app = new Vue({
      el: '#cat',
      data: {
        catImages: []
      },
      methods: {
        getCatImg: function () {
          const URL = 'https://api.thecatapi.com/v1/images/search'
          axios.get(URL)
            .then(response => {
              // console.log(response.data[0].url)
              this.catImages.push(response.data[0].url)
            })
        },
      }
    })
  </script>
</body>
</html>

```

# computed.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <div id="app">
    {{ message }}
    {{ reversedMessage }}
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        message: 'hello, vue'
      },
      // 해당 속성이 종속된 대상(message)이 변경될 때만 함수를 실행
      // 만약 아무 곳에도 의존하지 않는 computed 속성의 경우는 절대로 업데이트 되지 않는다.
      computed: {
        reversedMessage: function () {
          return this.message.split('').reverse().join('')
        }
      }
    })
  </script>
</body>
</html>

```

# computed_vs_method.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <div id="app">
    <button v-on:click="visible = !visible">toggle</button>
    <ul v-if="visible">
      <li>Method : {{ dateMethod() }}</li>
      <li>Computed : {{ dateComputed }}</li>
    </ul>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        visible: true
      },
      methods: {
        dateMethod: function () {
          return new Date()
        }
      },
      computed: {
        dateComputed: function () {
          return new Date()
        }
      }
    })
  </script>
</body>
</html>

```

# computed_vs_watch.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <div id="app">
    <h1>count : {{ count }}</h1>
    <h1>computed : {{ calculated }}</h1>
    <button @click="decreaseCount">메서드 실행</button>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        count: 5
      },
      methods: {
        decreaseCount: function () {
          this.count = this.count - 1
        }
      },
      computed: {
        calculated: function () {
          return this.count * 5
        }
      }, 
      watch: {
        // count가 변경될 때마다 해당 함수가 실행된다.
        // 이 때, 새로 변경된 값이 함수의 인자로 전달된다.
        count: function (args) {
          if (args === 0) {
            alert('count가 0이 됐습니다. 다시 초기화 하겠습니다.')
            this.count = 5
          }
        }
      }
    })
  </script>
</body>
</html>

```

