'''
양의 정수 N에 대해 N=x^3가 되는 양의 정수 x를 구하여라.
X가 존재하지 않으면 -1을 출력한다.
'''

arr = [i**3 for i in range(1000001)]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    #최소값 l, 최대값 r
    l, r = 1, 1000000
    # x가 존재하지 않으면 -1 출력
    ans = -1
    while l<=r:
        c=(l+r)//2
        if arr[c]==N:
            ans=c
            break
        #c**3이 N보다 작을땐, c값을 늘인다.
        if arr[c]<N:
            l=c+1
        # c**3이 N보다 클땐, c값을 줄인다.
        else:
            r=c-1
    print('#{} {}'.format(tc,ans))