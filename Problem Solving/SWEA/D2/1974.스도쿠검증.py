import sys
sys. stdin = open("input.txt","r")

T = int(input())
for tc in range(1, T+1):

    arr = [list(map(int, input().split())) for _ in range(9)]

    '''
    각 행의 합, 각 열의 합, 3X3 격자의 합이 모두 45이면 '1'출력/ 그렇지 않으면 '0'출력
    3X3 격자의 합을 구할 때는 중간점을 구해서 양사방을 탐색해서 더해주면 됨.
    그리고 마지막에 합, 열, 3X3의 합 모두 충족하는지 안 하는지 판별 해주면 됨.
    '''
    row_sum = []
    column_sum = []
    three_sum = []

    #각 행의 합
    for i in range(9):
        row_sum.append(sum(arr[i]))

    #각 열의 합
    for j in range(9):
        newcol = []
        for i in range(9):
            newcol.append(arr[i][j])   #sum(arr[i][j])가 아니라 arr[i][j]임.
        column_sum.append(sum(newcol))

    #3x3의 합
    dx = [-1,-1,-1,0,1,1,1,0,0]
    dy = [-1,0,1,1,1,-1,-1,-1,0]
    for i in range(1, 8, 3):
        for j in range(1, 8, 3):
            dir = []
            for d in range(9):
                dir.append(arr[i+dx[d]][j+dy[d]])
            three_sum.append(sum(dir))

    kkk = 0
    for i in range(9):
        if row_sum[i] != 45:
            print('0')
            kkk = 1
            break
        if column_sum[i] != 45:
            print('0')
            kkk = 1
            break
        if three_sum[i] != 45:
            print('0')
            kkk = 1
            break
    if kkk == 0:
        print('1')

