T=int(input())
for tc in range(1, T+1):
    N,M=map(int, input().split())   #10 3
    A=list(map(int,input().split()))
    suml=[]
    for i in range(N-M+1):
        suml.append(sum(A[i:i+M]))
    result=max(suml) - min(suml)
    print('#{} {}'.format(tc, result))















