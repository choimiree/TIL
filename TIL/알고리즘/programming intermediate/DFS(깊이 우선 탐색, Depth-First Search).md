# DFS(깊이 우선 탐색, Depth-First Search)

## DFS(1)(깊이 우선 탐색, Depth-First Search)

- **DFS(깊이 우선 탐색)**
  - 시작 정점에서 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색
  - 더 이상 갈 곳이 없게 되면, 가장 마지막에 만났던 갈림길 위치의 정점(vertex)으로 되돌아옴
  - 가장 마지막에 만났던 갈림길의 정점으로 되돌아가야 하므로 **후입선출 구조의 스택을 사용**



- **DFS 구현(1)**

  - 경로를 역추적할 때 필요한 자료구조 **스택**과 정점에 방문했는지에 대한 상태 정보를 저장하는 **visited 리스트**가 필요하다.

  1. DFS 호출되는 시점에 방문 시작 정점이 주어진다.

     --> 이 시작 정점을 변수 v에 할당.

  2. v를 visited에 방문했다고 표시한다.

  3. v와 인접한 정점 중 방문하지 않은 정점을 visited 리스트를 통해 찾는다.

     --> 이 중 하나의 정점을 선택해서 변수 w에 할당

  a: 방문할 정점의 정보가 있는 경우 // b: 방문할 정점의 정보가 없는 경우.

  a-4. 반문한 정점의 정보(v)를 stack에 저장. (=이후 되돌아 올 정점 정보)

  a-5. w를 방문, visited에 방문했다고 표시한다.

  a-6. w를 v변수에 할당하고 3~5 과정을 반복한다.

  -------------

  b-4. w가 빈 값이면 stack에서 pop하여 v에 저장한다.

  b-5. v와 인접한 정점 중 방문하지 않은 정점을 찾아 3~b-4 과정을 반복한다.

  b-6. Stack에서 pop하려 할 때 v가 빈 값이면 함수를 종료한다.

```python
#python 예시 - DFS(1): 재귀

def DFS(n):
    global field, visited, result
    if not visited[n]:
        visited[n] = 1
        result.append(n)
    for i in range(len(field)):
        if field[n][i] == 1 and not visited[i]:
            DFS(i)
            
V, E = 7,8
edgest = [1,2,1,3,2,5,2,4,3,5,4,6,5,6,6,7]
field = [[0] for i in range(V+1) for j in range(V+1)]
visited = [0 for i in range(V+1)]
result = []

for i in range(E):
    s,e=edges[i*2], edges[i*2+1]
    field[s][e] = 1
    field[e][s] = 1
    
DFS(1)
print(*result)

#출력
>>> 1 2 4 6 5 3 7
```

```python
#python 예시 - DFS(2): 스택

def DFS(n):
    global field, visited
    stack = [n]
    
    while stack:
        v = stack[-1]
        
        if not visited[v]:
            visited[v] = 1
            result.append(v)
            
        for i in range(len(field)):
            if field[v][i] == 1 and not visited[i]:
                stack.append(i)
                break
        else:
            stack.pop()
            
V, E = 7, 8
edges = [1,2,1,3,2,5,2,4,3,5,4,6,5,6,6,7]
field = [[0 for i in range(V+1)] for j in range(V+1)]
visited = [0 for i in range(V+1)]
result = []

for i in range(E):
    s,e = edges[2*i], edges[2*i+1]
    field[s][e] = 1
    field[e][s] = 1

DFS(1)
print(*result)

# 출력
>>> 1 2 4 6 5 3 7
         
```



## DFS(2)(깊이 우선 탐색, Depth-First Search)

- **DFS 구현(2)**
  - SW Expert Academy 1226 - [S/W 문제해결 기본] 7일차 - 미로1 [SW Expert Academy - Code - Problem (로그인 필요)](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14vXUqAGMCFAYD&categoryId=AV14vXUqAGMCFAYD&categoryType=CODE)

```python
#python 예시 - 미로1 DFS(1): 재귀

def DFS(y,x):
    global fiedl, visited, result
    dx = [1,0,-1,0] #우하좌상
    dy = [0,1,0,-1]
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        
        if not visited[ny][nx]:
            if field[ny][nx] == 0:
                visited[ny][nx] = 1
                DFS(ny, nx)
            elif field[ny][nx] == 3:
                result = 1
                return
            
for t in range(1, 11):
    T=int(input())
    field = [[i for i in list(map(int, input()))] for j in range(16)]
    visited = [[0 for i in range(16)] for j in range(16)]
    x = y= 0
    result = 0
    
    TF = False
    for i in range(16):
        for j in range(16):
            if field[i][j] == 2:
                x,y = j,i
                
    visited[y][x] = 1
    DFS(y,x)
    
    print('#{0} {1}'.format(t, result))
```

```python
#python 예시 - 미로1 DFS(2): 스택

def DFS(y,x):
    global field, visited, result
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    stack = [(y,x)]
    
    TF = False
    while stack:
        vy, vx = stack[-1]
        
        if not visited[vy][vx]:
            visited[vy][vx] = 1
        
        for i in range(4):
            ny = vy + dy[i]
            nx = vx + dx[i]
            if not visited[ny][nx]:
                if field[ny][nx] == 0:
                    stack.append((ny, nx))
                    break
                elif field[ny][nx] == 3:
                    result = 1
                    TF = True
                    return
        else:
            stack.pop()
            
for t in range(1, 11):
    T = int(input())
    field = [[i for i in list(map(int, input()))] for j in range(16)]
    visited = [[0 for i in range(16)] for j in range(16)]
    x = y = 0
    result = 0
    
    for i in range(16):
        for j in range(16):
            if field[i][j] == 2:
                x,y = j,i
                
    DFS(y,x)
    print('#{0} {1}'.format(T, result))
```











출처: SW Expert Academy - Learn - Course - Programming Intermediate

[SW Expert Academy - Programming Intermediate course](https://swexpertacademy.com/main/learn/course/subjectList.do?courseId=AVuPDN86AAXw5UW6)