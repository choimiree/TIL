# for tc in range(1, int(input())+1):
#     N = int(input())    #색칠한 사각형의 수
#     #10x10
#     arr = [[0] * 10 for _ in range(10)]
#     #N번 반복해서 사각영역의 정보를 읽어서 색칠한다.
#     ans = 0
#     for _ in range(N):
#         r1, c1, r2, c2, color = map(int, input().split())
#         # 행우선 탐색
#         for i in range(r1, r2+1):
#             for j in range(c1, c2+1):
#                 if arr[i][j] == 0 or 1 or 2:
#                     arr[i][j] += color
#                     if arr[i][j] == 3:
#                         ans += 1
#     print('#{} {}'.format(tc, ans))

#색이 겹쳐 보라색이 되는 칸의 수를 구하라
#왼쪽 위, 오른쪽 아래 인덱스, 칠할 색상이 주어진다.


T=int(input())
for tc in range(1,T+1):
    N=int(input())
    cnt=0
    #일단 빈 격자판 만들어줌
    pan = [[0]*10 for _ in range(10)]
    for _ in range(N):
        r1, c1, r2, c2, color = map(int,input().split())
    #보라색 찾는 거니까, 1 칠하고 2 칠해서 3인부분 찾으면 됨.
    #행우선탐색 시작
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if pan[i][j] == 0 or 1 or 2:
                    pan[i][j] += color
                    if pan[i][j] == 3:
                        cnt += 1
    print('#{} {}'.format(tc, cnt))














