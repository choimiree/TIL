for tc in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    Num_List = list(map(int, input().split()))
    for _ in range(M):
        I, Num = map(int, input().split())
        Num_List.insert(I, Num)
    print('#{} {}'.format(tc, Num_List[L]))