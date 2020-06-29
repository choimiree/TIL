#입력: '출발 도착 노드'라고 명시해놓은건 보통 '방향성 그래프'라 생각하면 됨.
    # E개의 줄 이후에는 경로의 존재를 확인할 출발 노드 S와 도착노드 G
#[반복]
def dfs(V,start,end):
    visited = [0] * (V+1)
    stack = []
    stack.append(start)
    while stack:
        n = stack.pop() #방문할 노드를 스택에서 꺼냄
        visited[n]=1    #현재 위치 n에 방문 표시
    if n == end:
        return 1
    for t in adj[n]:    #n의 인접 노드중
        if visited[t] == 0: #방문안한 노드를 스택에 추가
            stack.append(t)
    return 0

T = int(input())
for tc in range(1,T+1):
    V,E = map(int, input().split())
    adj = [[] for _ in range(V+1)] #인접리스트
    for _ in range(E):
        n1, n2 = map(int, input().split())
        adj[n1].append(n2)  #방향 그래프
        adj[n2].append(n1) #방향 없는 그래프면 이 과정 추가!
    start, end = map(int, input().split())
    print('#{} {}'.format(tc, dfs(V,start,end))) #1~V까지 노드가 있고, start~end까지 탐색해서 결과를 내달라는 말.

#---------------------------------------
#[재귀]
def dfs(n, end):
    if n == end:    #목적지면 1 반환
        return 1
    else:
        visited[n] = 1
        for t in adj[n]:
            if visited[t] == 0:
                if dfs(t,end) == 1: #return을 했는데 목적지를 찾은 경우
                    return 1
        return 0    #return을 했는데 목적지를 못찾은 경우

T=int(input())
for tc in range(1, T+1):
    V,E = map(int,input().split())
    adj = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    for _ in range(E):
        n1, n2 = map(int,input().split())
        adj[n1].append(n2)
    start,end = map(int,input().split())
    print('#{} {}'.format(tc, dfs(start, end)))
