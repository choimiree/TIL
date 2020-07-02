N=int(input())
for i in range(1, N+1):
    print('*'*i)
for j in range(2*N-1, N, -1):
    print('*'*(j-N))
