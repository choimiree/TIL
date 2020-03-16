for tc in range(1, int(input())+1):
    N = int(input())    #색칠한 사각형의 수
    #10x10
    arr = [[0] * 10 for _ in range(10)]
    #N번 반복해서 사각영역의 정보를 읽어서 색칠한다.
    ans = 0
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        # 행우선 탐색
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if arr[i][j] == 0 or 1 or 2:
                    arr[i][j] += color
                    if arr[i][j] == 3:
                        ans += 1
    print('#{} {}'.format(tc, ans))
