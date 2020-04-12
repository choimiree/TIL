#A와 B가 주어졌을 때 A를 입력하기 위한 최솟값을 구하여라.
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