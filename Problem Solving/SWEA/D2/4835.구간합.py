
for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    #구간의 시작위치 0~N-M
    Min = 1000000
    Max = 0
    for i in range(N-M+1):
        S = 0
        for j in range(M):#j = 0 ~ M-1 #시작위치부터 M개의 자료를 읽는다. --> 합
            S += arr[i+j]
        Min = min(Min, S) #최대,최소로 저장
        Max = max(Max, S)
    print(Max-Min)