# BFS(너비 우선 탐색, Breadth-First Search)

## BFS(너비 우선 탐색, Breadth-First Search)

- **BFS(너비 우선 탐색)**

  - 시작 정점에서 인접한 정점들을 모두 방문한 후,

    방문했던 정점을 시작점으로 해서 다시 인접한 정점을 방문하는 방식

  - 인접한 정점을 탐색한 후 차례로 BFS를 진행해야 하므로 **선입선출 구조의 큐를 사용**

- BFS 구현

  - 인접한 정점을 탐색하기 위한 자료구조 **큐**와 정점에 방문했는지에 대한 상태 정보를 저장하는 **visited 리스트**가 필요하다.

  1. BFS 호출되는 시점에 방문 시작 정점이 주어진다. 이 시작 정점을 큐에 넣어준다.

  2. while queue:

     시작점을 변수 v라고 하고, queue에서 원소하나를 빼내어 할당한다.

  3. v를 visited에 방문했다고 표시한다.

  4. v와 인접한 정점 중 방문하지 않은 정점을 visited리스트를 통해 찾고, 큐에 넣어준다.

  5. 큐에 원소가 없어질 때까지 2~4과정을 반복한다.

  ```python
  #python 예시 - BFS(1): list 활용
  
  def BFS(n):
      queue = [n]
      
      while queue:
          v = queue.pop(0)
          
          if no visited[v]:
              visited[v] = 1
              result.append(v)
              
          for i in range(len(field)):
              if field[v][i] == 1 and not visited[i]:
                  queue.append(i)
                  
  V,E=7,7
  edges = [1,2,1,3,2,5,3,5,4,6,5,6,6,7]
  field = [[0 for i in range(V+1)] for j in range(V+1)]
  visited = [0 for i in range(V+1)]
  result = []
  
  for i in range(E):
      s, e = edge[i*2], edges[i*2+1]
      field[s][e] = 1
      field[e][s] = 1
      
  BFS(1)
  print(*result)
  
  #출력
  >>> 1 2 3 5 6 4 7
  
  ```

  

  ``` python
  #python 예시 - BFS(2): collections.deque 활용
  
  from collections import deque
  
  def BFS(n):
      queue = deque()
      queue.append(n)
      
      while queue:
          v = queue.popleft()
          
          if not visited[v]:
              visited[v] = 1
              result.append(v)
              
          for i in range(len(field)):
              if field[v][i] == 1 and not visited[i]:
                  queue.append(i)
                  
  V, E =7, 7
  edges = [1,2,1,3,2,5,3,5,4,6,5,6,6,7]
  field = [[0 for i in range(V+1)] for j in range(V+1)]
  visited = [0 for i in range(V+1)]
  result = []
  
  for i in range(E):
      s,e = edges[i*2], edges[i*2+1]
      field[s][e] = 1
      field[e][s] = 1
      
  BFS(1)
  print(*result)
  
  #출력
  >>> 1 2 3 4 5 6 4 7
  
  ```

  



출처: SW Expert Academy - Learn - Course - Programming Intermediate

[SW Expert Academy - Programming Intermediate course](https://swexpertacademy.com/main/learn/course/subjectList.do?courseId=AVuPDN86AAXw5UW6)