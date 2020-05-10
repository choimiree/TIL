# 0시부터 다음 쉬는날 0시 전까지 A도크의 사용신청을 확인해
# 최대한 많은 화물차가 화물을 싣고 내릴 수 있도록 하며,
# 최대 몇대의 화물차가 필요할수있는지 알아내 출력.

import sys
sys.stdin = open("5202input.txt","r")

T=int(input())
for tc in range(1, T+1):
    N=int(input())
    lst = [[0]*2 for _ in range(N)]
    for i in range(N):
        lst[i] = list(map(int, input().split()))

    lst.sort(key=lambda x:x[1])
    end = lst[0][0]
    cnt = 1
    for i in range(1,N):
        if end <= lst[i][0]:
            end = lst[i][1]
            cnt += 1
    print('#{} {}'.format(tc, cnt))