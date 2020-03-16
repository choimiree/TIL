T = int(input())
for tc in range(1, T+1):
    maxmax = 0
    N = list(map(int, input().split()))
    maxx = []
    maxmax = max(N)
    for i in range(len(N)):
        maxx.append(maxmax)

    print('#{} {}'.format(tc, maxx[i]))

# a = int(input())
# k = []
# c = 0
# for i in range(a):
#     b = list(map(int, input().split(' ')))
#     c = max(b)
#
#     k.append((c))
#
# for i in range(0, a):
#     print('#{} {}'.format(i + 1, k[i]))