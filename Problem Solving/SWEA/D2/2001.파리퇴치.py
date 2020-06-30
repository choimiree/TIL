T=int(input())
for tc in range(1, T+1):

    N,M=map(int,input().split())    #5, 2
    arr = [list(map(int,input().split())) for _ in range(N)]
    # print(arr)

    #최대한 많은 파리를 죽여야 한다.
    new_arr =[]
    for i in range(N-M+1):
        for j in range(N-M+1):
            ls = []
            for m in range(M):
                ls += arr[i+m][j:j+M]
                b = sum(ls)
            new_arr.append(b)
        result=max(new_arr)
    print('#{} {}'.format(tc, result))