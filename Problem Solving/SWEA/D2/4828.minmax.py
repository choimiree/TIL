

T = int(input())
for tc in range(1, T + 1):
    # result = 0
    N = int(input())
    M = list(map(int, input().split()))
    a = max(M)
    b = min(M)
    print('#{} {}'.format(tc, a - b))

