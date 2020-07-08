# NxN에 파리의 개수
# MxM 크기의 파리채를 한 번 내리쳐 최대한 많은 파리를 죽이고자 한다.
# 5<=N<-15
# 2<=M<=N
# 각 영역 파리 개수 <= 30
T=int(input())
for tc in range(1, T+1):
    N,M=map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    flies=[]
    for x in range(N-M+1):
        for y in range(N-M+1):
            ls = []
            for i in range(M):
                # for j in range(M):
                ls += arr[x+i][y:y+M]
                sum_cnt = sum(ls)
            flies.append(sum_cnt)
    result = max(flies)
    print('#{} {}'.format(tc, result))
#
'''
T = int(input())
for tc in range(1, T+1):

    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    new_arr = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            ls = []
            for m in range(M):
                ls += arr[i+m][j:j+M]
                b = sum(ls)
            new_arr.append(b)
    c = max(new_arr)
    print('#{} {}'.format(tc, c))
'''