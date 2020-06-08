# vuex

> vue => data 변화 따라 (method 실행이 되고) DOM이 변화한다.

### state

> data

- 어떠한 상태를 관리한다.

### getters

> computed

- state를 변형 => 변수

### mutation

> methods

- 특징
  - state를 변경시키는 함수
  - 비동기 작업 포함 불가능

- 첫번째 인자로 `state` 를 받는다
- `commit` 을 통해서 호출한다.

### action

> mutation과 비슷, methods 종류

- 특징
  - state를 직접 mutation 시키는 것이 아니라,  `commit` 을 통해 `mutation` 을 호출한다
  - 비동기 작업도 포함이 된다.
- 첫번째 인자로 `context` 를 받는다
  - `state`, `commit`, `dispatch` 모두 가능
- `dispatch` 를 통해서 호출한다

---

### 헬퍼(helper)

> 편하게 불러오기 위한 도우미

- mapState
  - data, computed
- mapGetters
  - data, computed
- mapMutation
  - methods
- mapAction
  - methods