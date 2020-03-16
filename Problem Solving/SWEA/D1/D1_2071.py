T = int(input())
for tc in range(1, T+1):

    N = list(map(int, input().split()))
    average = 0
    for i in N:
        average += i
    print('#{} {}'.format(tc, round(average/len(N))))
