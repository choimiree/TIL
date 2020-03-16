
for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    Min = 10000  #나올 수 있는 최대값
    Max = 1      #나올 수 있는 최소값
    for i in range(1, N):
        if Min > arr[i]:
            Min = arr[i]
        if Max < arr[i]:
            Max = arr[i]

    print(Max-Min)

    # T = int(input())
    # for tc in range(1, T + 1):
    #     result = 0
    #     N = int(input())
    #     M = list(map(int, input().split()))
    #     a = max(M)
    #     b = min(M)
    #     print('#{} {}'.format(tc, a - b))