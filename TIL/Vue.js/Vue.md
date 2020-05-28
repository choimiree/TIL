# Vue

\- 지금까지 문서를 받는 행위를 해왔는데, 어느 순간 문서 전체를 받는게 힘들어지는 순간이 왔다.

\- 예를 들어, 댓글을 가져오거나 좋아요 버튼을 누를 때, 그거 하나 새로 랜더링하기 위해 전체페이지를 다시 받는 남용 문제가 발생했다. 

\- 원하는 데이터에 비해 전체적인 데이터를 받을 수 밖에 없는 상황인 것이다. 

\- 그래서 **axios library**를 사용한다.



## axios

\- 비동기(병렬: 여러 개가 동시 다발적으로 실행. 백그라운드에서 돌아가고 있는 여러 가지가 결과로 나와야 함) -> 실행한 callback 함수가 반드시 다시 돌아올 것이라는 약속!



\- axios의 리턴값 = Promise object라 생각하면 된다. 비동기 요청을 도와주는 라이브러리라 생각하면 된다.



\- axios library는 **vue.js**와 react에서 공식적으로 채택한 라이브러리이다. 



 



:hand: **만약, ''좋아요''와 같은 기능이 여러개라면?????**



\- ex) facebook: 친구 차단하면 -> 타임라인/친구목록/댓글목록/좋아요목록에서 모~두 차단한 친구의 흔적이 사라져야 함. -> 그러려면 모든 component끼리 연결되어 있어야 한다. 

\- 데이터, 유저와의 상호작용, 영향 받는 부분이 증가하는 것이다. 즉, Data의 변경에 따른 DOM 변화를 편하게 하기 위해 등장한 것!

\- 이를 해결하기 위해 front-end framework들이 하나둘 나타나기 시작한 것! ex) 구글 앵글러, react, 에반유 **Vue.js** 등

\- 결국, front-end framework들이 등장한 이유는, 사용자들의 경험을 가장 우선시했기 때문! **User Interface**를 만들기 위해 등장.

\- 우리는 그중에서도 **Vue**를 사용. react는 전부 javascript 쓴다. Vue는 template기반으로 쓰기 때문에.





## Vue의 instance

\- vue instance랑 그 instance가 조작할 dom이랑 binding해줘야 한다.

\- binding 되는 것은 view랑 viewmodel.

![image-20200525193826111](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20200525193826111.png)





### `el`

\- vue 인스턴스와 DOM을 연결(mount)하는 옵션

\- View(html element)와 ViewModel을 연결시켜준다.

\- id 혹은 class와 마운트 가능하다.

\- :stop_sign: vue인스턴스와 연결되지 않은 DOM 외부는 vue의 영향을 받지 않는다.



### `data`

\- 데이터 객체는 반드시 기본 개체`({})`여야 한다.

\- 객체 내부의 아이템들은 value로 모든 타입의 객체를 가질 수 있다. (object, string, integer, array,...)

\- data에서 정의된 속성은 인터폴레이션 `({{}})`을 통해 view에서 렌더링 가능

\- :stop_sign:data에서는 화살표 함수를 사용하면 안된다.



### `methods`

\- vue 인스턴스에 추가할 메서드들을 정의하는 곳

\- :stop_sign:화살표 함수를 메서드 정의하는데에 사용하면 안된다.