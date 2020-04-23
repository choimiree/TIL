#[4836. 색칠하기]
T = int(input())
for tc in range(1, T+1):

    paint_num = int(input())
    paint_in2 = [[0] * 10 for _ in range(10)]
    cnt = 0
    for k in range(paint_num):
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
    print('#{} {}'.format(tc, cnt))
