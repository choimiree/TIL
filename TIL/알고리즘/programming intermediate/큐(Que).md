# 큐(Que)

## 큐(1)

- **큐**
  - 스택처럼 삽입, 삭제의 위치가 제한적인 자료구조
  - 가장 먼저 삽입된 원소부터 삭제된다: 선입선출(FIFO, First-In-First-Out)
- 큐의 구조 및 연산
  - 큐에 저장된 원소 중 첫 번재 원소를 머리(Front)라고 하고, 마지막 원소를 꼬리(Rear)라고 한다.
  - 큐 관련 연산
    - enQueue(item): 저장소에 자료 저장(큐의 꼬리에 원소 삽입)
    - deQueue(): 저장소에서 자료를 꺼냄(큐의 머리에서 삭제하고 반환, 선입선출)
    - Qpeek: 큐의 머리에서 원소를 삭제하지 않고 반환하는 연산
    - createQueue(): 공백 상태의 큐를 만드는 연산
    - isEmpty(): 큐가 공백인지 확인하는 연산
    - isFull(): 큐가 포화상태인지 확인하는 연산
- 큐의 종류
  - 선형 큐, 원형 큐, 연결 큐, 우선순위 큐
    - 선형 큐, 원형 큐: 리스트를 사용해서 구현
    - 연결 큐: 연결 리스트를 사용해서 구현



## 큐(2) - 큐의 종류

- 선형 큐

  - 1차원 리스트를 활용한다. (큐의 크기 == 리스트의 크기)
  - front - 머리 인덱스 // rear - 꼬리 인덱스
    - 초기: front = rear = -1
    - 공백: front == rear
    - 포화: rear == len(lst)-1 (꼬리 인덱스가 리스트의 마지막 인덱스가 되면 포화)

- 선형 큐 구현하기

  1. 기본 세팅

     - 초기화 함수: CreateQueue()

       크기 n인 1차원 리스트를 만들고 front = rear = -1로 설정

       (고정된 크기의 리스트를 사용)

     - 공백 상태 체크 함수: isEmpty()

       front == rear이면 True를 반환하는 함수

     - 포화 상태 체크 함수: isFull()

       rear == len(lst)-1이면 True를 반환하는 함수

  2. 연산

     - 삽입: enQueue(item)

       - 큐가 포화 상태인 경우 삽입하지 못함
       - rear 값을 +1 한 후 [rear] 자리에 item을 저장

     - 삭제: deQueue()

       - 큐가 공백 상태인 경우 삭제하지 못함

       - front 값을 +1한 후 [front]자리의 item을 반환

         (front값을 +1해주기 때문에 리스트에서 원소를 별도로 삭제해줄 필요가 없다.)

     - 검색: Qpeek()

       - 큐의 가장 앞에 있는 원소를 찾아서 반환

       - [front+1] 자리의 item을 반환

         (큐에서 item이 삭제되지 않는 이유는 front 값을 바꾸지않기 때문이다.)

         

- 선형 큐의 문제점

  - 고정된 리스트를 사용하기 때문에 사용할 큐의 크기 만큼의 공간을 미리 확보해야 한다. 이때문에 메모리 낭비가 발생한다.
  - 삽입, 삭제를 하다보면 리스트의 앞부분에 활용할 수 있는 공간이 있더라도 꼬리가 len(lst)-1에 도달하면 큐가 포화된 것으로 인식되어 더이상 큐를 사용할 수 없다.



- **원형 큐**

  - 선형 큐와 같은 방식이지만, 머리와 꼬리를 붙여 원형을 이룬다고 생각한다.

    - 이 방식을 구현하기 위해 인덱스를 순환해야 하므로 %연산자를 사용한다.

  - front - 머리 인덱스 // rear - 꼬리 인덱스

    - 초기: front = rear = 0
    - 공백: front == rear
    - 포화: (rear+1)%len(lst) == front(rear의 다음 위치 == front)

    > 공백, 포화 상태를 쉽게 구분하기 위해 front 자리는 항상 비워둠.

- 원형 큐 구현하기

  1. 기본 세팅

     - 초기화 함수: CreateQueue()

       크기 n인 1차원 리스트를 만들고 front = rear = 0으로 설정

       (고정된 크기의 리스트를 사용)

     - 공백 상태 체크 함수: isEmpty()

       front == rear 이면 True를 반환하는 함수

     - 포화 상태 체크 함수: isFull()

       (rear + 1)%len(lst) == front 이면 True를 반환하는 함수

  2. 연산

     - 삽입: enQueue(item)

       - 큐가 포화 상태인 경우 삽입하지 못함
       - rear = (rear + 1)%len(lst) 한 후 [rear]자리에 item을 저장

     - 삭제: deQueue()

       - 큐가 공백 상태인 경우 삭제하지 못함

       - front = (front+1)%len(lst) 한 후 [front]자리의 item을 반환

         (원소가 남아있더라도 rear가 다시 그 위에 정보를 덮어쓰기 때문에 리스트에서 원소를 별도로 삭제해줄 필요가 없다.)



- 원형큐의 문제점

  - rear 또는 front가 배열의 끝까지 가면 배열의 앞부분으로 이동해야 한다.

    이때 rear이나 front를 이동하기 위한 연산이 필요하고, 이를 위해 추가적인 시간이 소모되므로 큐의 효율이 낮아진다.

  - 선형 큐와 마찬가지로 포화 상태가 되면 더이상 큐를 사용할 수 없다.



- 파이썬의 리스트를 활용한 큐
  - 파이썬의 리스트는 크기를 동적으로 변경할 수 있어서 메모리를 절약할 수 있다.
  - 하지만 큐를 구현하는 도중에 정보를 삽입, 삭제, 이동하는 연산을 수행하는 데 많은 시간이 걸린다는 단점이 있다.



- **연결 큐**

  - 단순 연결 리스트를 활용한다.
    - 큐의 원소: 단순 연결 리스트의 각 노드
    - 큐의 원소 순서: 노드의 연결 순서(링크로 연결됨)
  - front - 첫번째 노드를 가리키는 링크// rear-마지막 노드를 가리키는 링크
    - 초기: front = rear = None
    - 공백: front = rear- = None
    - 포화: 없음(계속 노드를 추가할 수 있기 때문에 연결 큐에서는 포화상태가 없다.)

- 연결 큐 구현하기

  1. 기본 세팅

     - 초기화 함수:  CreateLinkedQueue()

       front = None, rear = None으로 설정(포인터 변수만 생성)

     - 공백 상태 체크 함수: isEmpty()

       front = rear = None이면 True를 반환하는 함수

     - 포화 상태 체크 함수: 필요없음

  2. 연산

     - 삽입: endQueue(item)

       - 새로운 노드를 만들고 데이터로 item을 저장

       - 연결 큐가 공백인 경우: front, rear 모두 해당 노드로 링크한다.

         연결 큐가 공백이 아닌 경우: rear만 해당 노드로 링크한다.

     - 삭제: deQueue()

       - 큐가 공백 상태인 경우 삭제하지 못함

       - front을 다음 노드로 링크시켜준다.

         --> 다음노드로 링크시키기 전에 기존의 노드를 따로 저장해두고 반환한다.

       - 삭제 후 공백 큐가 되는 경우 rear도 None으로 설정한다.



- **큐 모듈** - import해서 사용 가능(import queue)

  - 큐 모듈의 클래스

    - qeueu.Queue(maxsize=0)

      : 선입선출 큐의 생성자.

      maxsize는 큐에 배치할 수 있는 항목 수의 상한이며 0보다 작거나 같으면 큐의 크기는 무한하다.

    - queue.LifoQueue(maxsize=0)

      : 후입선출 큐의 생성자(사실상 스택의 개념) maxsize는 위와 동일.

    - queue.PriorityQueue(maxsize=0)

      : 우선순위 큐의 생성자. maxsize는 위와 동일

      : 가장 낮은 값을 갖는 항목이 먼저 꺼내진다.

      --> 항목의 전형적인 패턴은 (priority_number, data) 형식의 튜플이며 가장 낮은 값을 갖는 항목은 sorted(list(entries))[0]에 의해 반환되는 항목이다.

  - 본 클래스들의 메서드

    - qsize()

      : 큐의 크기를 반환

    - put(item, block=True, timeout=None)

      : 큐에 item을 넣는다.(삽입)

    - get(block= True, timeout=None)

      : 큐에서 항목을 제거하고 반환한다.(삭제)

      :큐 전체 특성에 맞추어 반환합니다.

      (ex. 우선순위 큐와 다른 큐의 get결과 값은 다를 수 있다.)

    - empty()

      : 큐가 비어 있으면 True, 아니면 False를 반환한다.

    - full()

      : 큐가 가득 차면 True, 아니면 False를 반환한다.



## 큐(3) - deque(덱)

- collections.deque([literable[, maxlen]])(from collections import deque)

  - literable의 데이터를 왼쪽에서 오른쪽으로 나열한 덱 객체를 생성한다.

    (literable가 입력되지 않으면 빈 덱 객체를 생성한다.)

  - deque = double-ended queue

    덱의 양쪽 어느 방향이든 append, pop의 시간 복잡도가 O(1)이다.

    - 고정된 길이 내에서 **접근(or 검색), 슬라이싱**을 하는 데에는 **list**가 유리하지만, 데이터를 **추가 or 삭제**할 땐 **deque**가 유리하다.

  - maxlen이 입력되지 않거나 None이면 덱의 길이는 무한히 커질 수 있다.

    maxlen이 입력된다면 덱의 길이는 maxlen 만큼의 상한을 가진다.

    - 덱의 길이가 정해졌을 때 새로운 항목이 추가되면 반대쪽 끝에 있는 항목이 삭제된다.

      - **list, deque 안에서 작업에 따른 시간복잡도 비교**

      

  - **deque의 메소드**

    - list에 사용되는 함수와 같은 역할을 하는 메소드

      - append(x)
      - clear()
      - copy()
      - count(x)
      - extend(iterable)
      - index(x[, start[, stop]])
      - insert(i, x)
      - len(d)
      - pop()
      - remove(value)
      - reverse()
      - reversed(d)

    - list에 사용되는 함수와 차이 있는 메소드

      - appendleft(x): 덱의 왼쪽 부분에 x를 더한다.

      - extendleft(iterable): 덱의 왼쪽 부분에 iterable의 데이터를 항목 별로 추가한다. 이때 iterable 안에서 순서의 역순으로 추가된다.

        ex) a가 빈 덱일 때, a.extendleft([1,2,3,4]) --> deque([4,3,2,1])

      - popleft(): 덱의 왼쪽 부분에서 데이터를 삭제하여 반환한다.

      - rotate(n=1): 덱을 오른쪽으로 n차례 회전시킨다. n이 음수라면 왼쪽으로 회전한다.

      - maxlen: 덱의 최대 크기를 나타낸다. 크기가 정해져있지 않다면 None을 반환한다.

      - 슬라이싱: itertools를 import해와서 해야 한다.

      ```python
      #python 예시 - 덱 슬라이싱
      
      from collections import deque
      import itertools
      
      q=deque([1,2,3,4,5])
      print(q)
      print(list(itertools.islice(q,1,3)))
      
      # islice(iterable, *args)
      # islice('ABCDEFG', 2) --> A B
      # islice('ABCDEFG', 2, 4) --> C D
      # islice('ABCDEFG', 2, None) --> C D E F G
      # islice('ABCDEFG', 0, None, 2) --> A C E G
      # 슬라이싱 하고 싶은 iterable 변수를 넣어주고,
      # 그 후 입력되는 인자는 슬라이싱 할 때와 같은 방식으로 한다.
      
      #출력
      >>> deque([1,2,3,4,5])
      >>> [2,3]
      
      ```


  

  ## 큐(4) - 우선순위 큐 개요

  - 우선순위 큐

    - 우선순위를 가진 항목들을 저장하는 큐
    - **우선순위가 높은 것부터** 먼저 나가게 됨(우선순위가 같은 것끼리는 선입선출)

  - 우선순위 큐 구현하기

    1. 방법: 리스트를 사용하여 구현 or 우선순위 큐 라이브러리 사용

    2. 연산:

       1. 기본 세팅: 큐의 구조랑 같다.

       2. 삽입(enQueue): 우선순위에 맞는 위치에 데이터를 삽입한다.

          삭제(deQueue): 가장 앞에 있는 원소를 삭제하고 반환한다.

          (가장 우선순위가 높다.)

  - 우선순위 큐를 리스트를 활용해서 구현할 때의 문제점

    - 데이터를 삽입하거나 삭제할 때 원소를 재배치하며 시간이 많이 걸리고 메모리 낭비가 크다.
    - 연결 리스트로 우선순위 큐를 구현하더라도 비교 연산이 많이 필요하다.

  - 문제점 해결 방법

    - priorityQueue(maxsize) 클래스 사용
    - 힙 자료구조 사용

  

  

  



출처: SW Expert Academy - Learn - Course - Programming Intermediate

[SW Expert Academy - Programming Intermediate course](https://swexpertacademy.com/main/learn/course/subjectList.do?courseId=AVuPDN86AAXw5UW6)