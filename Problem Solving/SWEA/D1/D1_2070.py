
T = int(input())
for tc in range(1, T+1):

    same = '='
    right = '<'
    left = '>'
    compare = []

    N = list(map(int, input().split(' ')))
    for i in range(len(N)):

        if int(N[0]) == int(N[1]):
            compare.append(same)
        elif int(N[0]) < int(N[1]):
            compare.append(right)
        else:
            compare.append(left)

    print('#{} {}'.format(tc, compare[i]))