T=int(input())
for tc in range(1, T+1):
    N,M=map(int,input().split())
    W=list(map(int,input().split()))
    T_lst=list(map(int,input().split()))
    W.sort(reverse=True)
    T_lst.sort(reverse=True)

    count = 0
    while W:
        k=W.pop(0)
        if len(T_lst) != 0:
            for i in range(len(T_lst)):
                if T_lst[i] >= k:
                    count = count + k
                    T_lst.pop(i)
                    break
    print('#{} {}'.format(tc, count))