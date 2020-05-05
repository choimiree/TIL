##두 개의 숫자열
for tc in range(1, int(input())+1):
    N,M=map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))

    #A와B의 수열의 길이에 주의
    if N > M:
        A, B = B, A  #A:짧은 수열, B: 긴 수열
        N, M = M, N  #N:짧은 수열, M: 긴 수열

    #길이가 N인 구간의 모든 시작 위치에 대해
    Max = -100000000
    for i in range(M-N+1):
        S = 0
        for j in range(N):
            S += (A[j] + B[i+j])
        Max = max(Max, S)
