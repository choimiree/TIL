# NxN 크기의 미로에서 출발지, 목적지가 주어진다.
#이때 최소 몇 개의 칸을 지나면 출발지에서 도착지에 다다를 수 있는지 알아내는 프로그램을 작성하시오.
#경로가 있는 경우 출발에서 도착까지 가는데 지나야 하는 최소한의 칸 수를, 경로가 없는 경우 0을 출력한다.
#다음은 5x5 미로의 예이다. 1은 벽, 0은 통로를 나타내며 미로 밖으로 벗어나서는 안된다.
# 13101
# 10101
# 10101
# 10101
# 10021
#마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 5개의 칸을 지나 도착할 수 있다.
# 입력: 5<=N<=100
# 0은 통로, 1은 벽, 2는 출발, 3은 도착.
dx = [0, 1, 0, -1] #우하좌상
dy = [1, 0, -1, 0]

def maze(i, j): #탐색 시작점
    global stop
    for k in range(4):
        if M[i+dx[k]][j+dy[k]] == 0 or M[i+dx[k]][j+dy[k]] == 3:
            if V[i+dx[k]][j+dy[k]] == 0:
                Q.append([i+dx[k], j+dy[k]])    #시작점을 큐에 삽입
                V[i+dx[k]][j+dy[k]] += V[i][j] + 1  #방문한 것으로 처리하고 다른 칸으로
T=int(input())
for tc in range(1, T+1):
    N=int(input())
    M=[[1] + list(map(int,input().split())) + [1] for _ in range(N)]    #벽두른 기본 미로판
    M=[[1]*(N+2)] + M + [[1]*(N+2)] #벽두른 기본 미로판
    V=[[0]*(N+2) for _ in range(N+2)]   #정점의 개수 + 판
    Q=[]    #큐생성
    result = 0

    for i in range(N+2):
        for j in range(N+2):
            if M[i][j] == 2:
                Q.append([i,j])
                V[i][j] += 1
                maze(i,j)
            while Q:
                move = Q.pop(0)
                if M[move[0]][move[1]] == 3:
                    result = V[move[0]][move[1]]
                    break
                else:
                    maze(move[0], move[1])

    if result == 0:
        print('#{} {}'.format(tc, result))
    else:
        print('#{} {}'.format(tc, result-2))