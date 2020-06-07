#bfs
#인접행렬
def bfs(v):
    global f,r
    #enQueue
    r += 1
    Q[r] = v
    visit[v] = 1

    while (f != r): #Not empty
        #dequeue
        f += 1
        v = Q[f]
        if visit[v] > 3:    return

        for i in range(N+1):
            if G[v][i] and not visit[i]:
                #enqueue
                r += 1
                Q[r] = i
                visit[i] = visit[v] + 1

T=int(input())
for tc in range(1, T+1):
    N,M=map(int,input().split())
    G=[[0 for _ in range(N+1)] for _ in range(N+1)]
    ans = 0
    Q = [0] * (N*N)
    f = -1
    r = -1
    visit = [0] * (N+1)
    for i in range(M):
        u,v = map(int,input().split())
        G[u][v]=G[v][u]=1
    bfs(1)
    for i in range(N+1):
        if visit[i] == 2 or visit[i] == 3:
            ans += 1
    print("#{} {}".format(tc, ans))