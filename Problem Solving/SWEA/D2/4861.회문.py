# ABBA처럼 어느 방향에서 읽어도 같은 문자열을 회문이라 한다.
# NxM 크기의 글자판에서 길이가 M인 회문을 찾아 출력하라.
# 회문은 1개가 존재하는데, 가로뿐만 아니라 세로로 찾아질 수도 있다.
# 입력: 1<=T<=50, 10<=N<=100, 5<=M<=N
def f(N, M):
    for i in range(N):  # 가로회문
        for j in range(N - M + 1):
            for k in range(M // 2):
                if s[i][j + k] != s[i][j + M - 1 - k]:
                    break
                if k == M // 2 - 1:
                    return i, j, 0
        for j in range(N):  # 세로회문
            for i in range(N - M + 1):
                for k in range(M // 2):
                    if s[i + k][j] != s[i + M - 1 - k][j]:
                        break
                    if k == M // 2 - 1:
                        return i, j, 1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    s = [input() for i in range(N)]
    i, j, v = f(N, M)
    print('#{}'.format(tc), end=' ')
    if v == 0:
        for h in range(M):
            print(s[i][j + h], end='')
        print()
    else:
        for h in range(M):
            print(s[i + h][j], end='')
        print()