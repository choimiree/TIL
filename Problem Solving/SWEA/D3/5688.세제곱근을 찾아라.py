arr = [i**3 for i in range(1000001)]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    l, r = 1, 1000000
    ans = -1
    while l<=r:
        c=(l+r)//2
        if arr[c]==N:
            ans=c
            break
        if arr[c]<N:
            l=c+1
        else:
            r=c-1
    print('#{} {}'.format(tc,ans))