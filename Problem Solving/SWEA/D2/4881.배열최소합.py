def f(n,k,s):   #n은 순열의 인덱스, s는 생성된 부분까지의 합
    global minV
    if n == N:  #순열이 완성된 경우
        if minV>s:  #기존의 최소값보다 작으면
            minV=s
        return
    elif minV <= s: #순열이 완성되지 않았찌만 합이 최소값보다 큰 경우
        return
    else:
        for i in range(k):  #순열의 n번 인덱스에 들어갈 숫자 선택
            if u[i] === 0:
                u[i] = 1
                find(n+1, k, s+m[n][i])
                u[i] = 0
            return

T = int(input())
for tc in range(1, T+1):
    N=int(input())
    A=[list(map(int,input().split())) for _ in range(N)]
    used=[0]*N
    minV=100
    f(0,N,0)
    print('#{} {}'.format(tc, minV))

