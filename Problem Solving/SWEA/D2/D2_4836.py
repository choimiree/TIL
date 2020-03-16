tc = int(input())
for test_case in range(tc):

    round = int(input())


    paint_in = []
    paint_in2 = []
    cnt = 0

    #ls = [list(map(int, input().split())) for _ in range(100)]
    for i in range(10):
        for i in range(10):
            paint_in.append(0)
    for i in range(10):
        paint_in2.append(paint_in[i * 10:10 + (i * 10)])

    for k in range(round):
        temp = list(map(int, input().split()))

        for i in range(10):
            for j in range(10):
                if i >= temp[0] and i <= temp[2]:
                    if  j>= temp[1] and j <= temp[3]:
                        # 색이 겹칠떄(이미 색이 들어와 있다면 )어떻게 처리할지
                        if paint_in2[i][j] == 1 or paint_in2[i][j] == 2:
                            cnt += 1
                        else:
                            paint_in2[i][j] = temp[4]

    print('#{} {}'.format(test_case+1, cnt))