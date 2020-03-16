T= int(input())
for tc in range(1, T+1):

    result = 0
    remain = 0
    N = list(map(int, input().split()))
    result = N[0]//N[1]
    remain = N[0]%N[1]
    print('#{} {} {}'.format(tc, result, remain))