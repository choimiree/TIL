dx = [-1,-1,-1,0,1,1,1,0] #8방향 탐색을 위해서 행과 열을 더 해 줄 값
dy = [-1,0,1,1,1,0,-1,-1]

T = int(input())
for tc in range(1, T+1):
    N,M = list(map(int, input().split())) #N: 보드판, M:돌을 놓는 횟수

    #게임판의 상태를 저장
    pan = [[0]*(N+1) for _ in range(N+1)]
    #초기 게임판의 상태를 설정
    p = N//2
    pan[p][p] = pan[p+1][p+1] = 2 #백
    pan[p+1][p] = pan[p][p+1] = 1 #흑

    #M번의 돌을 두는 정보 처리
    for _ in range(M):
        x,y,dol = map(int, input().split())
        pan[x][y] = dol

        for i in range(8):
            tx,ty = x+dx[i], y+dy[i]

            while 1 <=tx<= N and 1<=ty<=N:
                if pan[tx][ty] == 0:
                    break
                if pan[tx][ty] == dol:
                    #tx,ty ---> x,y
                    while tx != x or ty != y:
                        pan[tx][ty] = dol
                        tx, ty = tx - dx[i], ty - dy[i]
                    break
                tx, ty = tx + dx[i], ty + dy[i]
    # pan[][]에 저장된 1의 개수 2의 개수를 카운팅해서 정답 출력
    black = 0
    white = 0
    for b in range(N+1):
        for w in range(N+1):
            if pan[b][w] == 1:
                black += 1
            elif pan[b][w] == 2:
                white += 1

    print('#{} {} {}'.format(tc, black, white))


