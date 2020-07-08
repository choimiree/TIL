#내방식
#     각 행의 합, 각 열의 합, 3X3 격자의 합이 모두 45이면 '1'출력/ 그렇지 않//으면 '0'출력
#     3X3 격자의 합을 구할 때는 중간점을 구해서 양사방을 탐색해서 더해주면 됨.
#     그리고 마지막에 합, 열, 3X3의 합 모두 충족하는지 안 하는지 판별 해주면 됨.
# T=int(input())
# for tc in range(1, T+1):
#     arr = [list(map(int,input().split())) for _ in range(9)]
#     #3x3, 각 행, 각 열이 45이면 1, 그렇지 않으면 0
#     #3x3의 경우. 중간지점을 선택해서 양 사방을 탐색
#     dx=[-1,-1,-1,0,1,1,1,0,0]
#     dy=[-1,0,1,1,1,0,-1,-1,0]
#     three_sum=[]
#     for x in range(1,8,3):
#         for y in range(1,8,3):
#             three=[]
#             for d in range(9):
#                 three.append(arr[x+dx[d]][y+dy[d]])
#             three_sum.append(sum(three))
#
#     #각행의 합
#     row_sum=[]
#     for i in range(9):
#         row_sum.append(sum(arr[i]))
#
#     #각열의 합
#     col_sum=[]
#     for j in range(9):
#         new_col = []
#         for i in range(9):
#             new_col.append(arr[i][j])
#         col_sum.append(sum(new_col))
#     #이제 3부분의 합이 45인지 아닌지 판단해서 1, 0 출력하게끔
#     kkk=0
#     for k in range(9):
#         if three_sum[k] != 45:
#             print('#{} {}'.format(tc, 0))
#             kkk = 1
#             break
#         if col_sum[k] != 45:
#             print('#{} {}'.format(tc, 0))
#             kkk = 1
#             break
#         if row_sum[k] != 45:
#             print('#{} {}'.format(tc, 0))
#             kkk = 1
#             break
#     if kkk == 0:
#         print('#{} {}'.format(tc, '1'))

T=int(input())
for tc in range(1,T+1):
    arr=[list(map(int,input().split())) for _ in range(9)]
    #가로줄, 세로줄, 3x3의 합에 있는 숫자가 겹치지않으려면 각 합이 45로 동일해야한다.
    #가로줄부터
    row_sum=[]
    for i in range(9):
        row_sum.append(sum(arr[i]))

    #세로줄
    col_sum=[]
    for j in range(9):
        new_col = []
        for i in range(9):
            new_col.append(arr[i][j])
        col_sum.append(sum(new_col))

    #3x3
    dx=[-1,-1,-1,0,1,1,1,0,0]
    dy=[-1,0,1,1,1,0,-1,-1,0]
    three_sum=[]
    for i in range(1, 8, 3):
        for j in range(1, 8, 3):
            three=[]
            for d in range(9):
                three.append(arr[i+dx[d]][j+dy[d]])
            three_sum.append(sum(three))

    if cnt == 3:
        print('#{} {}'.format(tc, '1'))
    else:
        print('#{} {}'.format(tc, '0'))