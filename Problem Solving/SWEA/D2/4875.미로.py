'''
NxN크기의 미로에서 출발지에서 목적지에 도착하는 경로가 존재하는지 확인하는 프로그램을 작성하시오.
도착할 수 있으면 1, 아니면 0을 출력한다.
주어진 미로 밖으로는 나갈 수 없다.
0은 통로, 1은 벽, 2는 출발, 3은 도착. 5<=N<=10
'''
def f(sRow, sCol, N):
    dRow = [0,1,0,-1]
    dCol = [1,0,-1,0]
    s=[]
    s.append([sRow,sCol])   #입구로 이동
    maze[sRow][sCol]=1  #방문 표시
    while s:    #스택에 좌표가 남아있으면
        row, col = s.pop()  #갈수 있는
        if maze[row][col] == 3: #출구인 경우
            return 1
        for i in range(4):  #주변 좌표 계산
            nRow = row + dRow[i]
            nCol = col + dCol[i]
            if 0 <= nRow < N and 0 <= nCol < N: #미로 내부
                if maze[nRow][nCol] != 1:   #갈 수 있는 곳 저장
                    s.append([nRow,nCol])
                    maze[row][col] = 1
    return 0    #출구에 가지 못하고 끝나는 경우

T=int(input())
for tc in range(1, T+1):
    N=int(input())
    maze = [[int(x) for x in input()] for _ in range(N)]    #미로를 저장
    # print(maze)
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sRow, sCol = i, j   #출발 row index
    print('#{} {}'.format(tc, f(sRow,sCol,N)))
