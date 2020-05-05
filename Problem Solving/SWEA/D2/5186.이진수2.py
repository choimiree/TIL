import sys

sys.stdin = open('5186.txt', 'r')

T=int(input())
for tc in range(1, T+1):
    n = float(input())
    ans = ''
    cnt = 0
    while cnt < 13:
        next = n * 2
        ans += str(int(next))
        n = next - int(next)
        cnt += 1
        if n == 0:
            break

    if cnt >= 13:
        ans = 'overflow'

    print('#{} {}'.format(tc, ans))
