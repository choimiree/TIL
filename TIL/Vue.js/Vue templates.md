# Vue templates

### vue component 구조

- template
- script
- style



### 컴포넌트를 사용하는 단계

1. 컴포넌트 생성 (.vue)

2. **template**

   기존 : <div id="app"></div>

   html 코드를 작성하는 부분

   div태그 안에 작성하자!

3. **script**

   js 코드를 작성하는 부분

   기존 : const app = new Vue({})

4. **style**

   css 코드를 작성하는 부분

5. App.vue에서작성해주기

   1. script에 불러오기

   2. script에 등록하기
   
   3. template 사용하기
   
   div를 최상단으로 하고 그 안에 작성한다.

>  흐름: 가져오고  -> 등록하고 -> 사용하기!



### router 등록 단계

1. views의 컴포넌트 생성(.vue)
2. router/index.js에 router를 등록
3. App.vue에 router-link 작성



### components랑 views를 왜 구분??

1. **views**

- 한 페이지 전체

2. **components**

- 일부분(부품)

#### 공통점

- 둘 다 Vue 컴포넌트다.

#### 차이점

- views 폴더 안에 있는 컴포넌트는 routing에 매핑되는 컴포넌트다.
- 이 경로는 `router/index.js` 에 정의하게 된다.

- Vue Router를 사용하게 되면 `<router-link></router-link>` 태그를 활용해 해당 컴포넌트의 routing을 매핑하고, `<router-view/>` 태그를 활용해 특정 부분에 컴포넌트를 렌더링한다.

#### 결론

- 사실 자신에게 맞는 방식과 구조로 작성할 수 있다.
- 일종의 컨벤션일 뿐.

