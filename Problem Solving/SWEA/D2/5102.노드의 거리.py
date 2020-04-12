for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    pan = [[0] * (V+1) for _ in range(V+1)]

    for n in range(E):
        i, j = map(int, input().split())
        pan[i][j] = 1
        pan[j][i] = 1
    S,G = map(int, input().split())
    W = [0] * (V+1) #visited
    Q = [] #queue생성
    result = 0

    for i in range(1, V+1):
        if pan[S][i] == 1:
            Q.append(i)
            W[S], W[i] = 1,1

    while Q:
        move = Q.pop(0)
        if move == G:
            result = W[move]
            break
        for j in range(1, V+1):
            if pan[move][j] == 1 and W[j] == 0:
                Q.append(j)
                W[j] = W[move] + 1

    print('#{} {}'.format(tc, result))