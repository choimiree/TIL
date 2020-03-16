#[ 교재18page ]
#총26개의 상자가 회전 후, 오른쪽 방 그림의 상태가 된다. A상자의 낙차가 7로 가장 크므로 7을 리턴하면 된다.
#회전 결과, B상자의 낙차는 6, C상자의 낙차는 1이다.
arr = [7,4,2,0,0,6,0,7,0]
N = len(arr)
#arr[0] --> arr[N-1] 까지 낙차값 (밑에 오는 상자들이 없다면)
#모든 꼭대기의 상자에 대해서 반복 수행
ans = 0
for i in range(N):
    h = N - 1 - i #상자의 위치에서 바닥까지 거리
    if ans >= h:
        break
    # 자기 밑에 오는 상자의 수를 카운팅
    for j in range(i+1, N):
        if arr[i] <= arr[j]: #밑에 오는 상자
            h -= 1
    ans = max(ans, h)

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












