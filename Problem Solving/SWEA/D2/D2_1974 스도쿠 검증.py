import sys
sys. stdin = open("input.txt","r")

T = int(input())
for tc in range(1, T+1):

    arr = [list(map(int, input().split())) for _ in range(9)]

    # 행, 열, 3x3의 합이 45가 될 때 '1' 그렇지 않을 때 '0'
    row_sum = []
    column_sum = []
    three_sum = []

    for i in range(9):                      #각 행에 있는 요소들의 합 리스트에 담아줌.
        row_sum.append(sum(arr[i]))


    for j in range(9):   #각 열에 있는 요소들의 합을 더해주려면 각 행을 더해주는 것이랑은 좀 다름. 각 열에 있는 첫번째 요소들을 담아주는 리스트를 다시 만들어주고 나서 다시 열의 합 리스트에 넣어야 함.
        rownew = []
        for i in range(9):
            rownew.append(arr[i][j])
        column_sum.append(sum(rownew))

    dx = [-1, -1, -1, 0, 1, 1, 1, 0, 0]     #3x3 좌표에 있는 거 더해주는 리스트를 만들려면 일단 중간 좌표를 잡아서 사방을 탐색한 후에 이걸 다 더해주면 됨.
    dy = [-1, 0, 1, 1, 1, 0, -1, -1, 0]
    for i in range(1, 8, 3):
        for j in range(1, 8, 3): #3x3의 가운데 좌표
            dir = []
            for d in range(9):
                dir.append(arr[i+dx[d]][j+dy[d]]) ##이때 각 좌표의 양사방에 있는 좌표 잘 설정해줘야 함.
            three_sum.append(sum(dir))

    kkk = 0                 #kkk=0은 답이 잘 안나와서 그냥 변수 설정해준거임. kkk=0으로 변수 설정하고 나중에 kkk=0이 그대로 있으면 for문 안에 있는 것이 만족 안한다는 거니까 이렇게 해주면 됨.
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