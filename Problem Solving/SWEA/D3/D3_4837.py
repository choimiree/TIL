# 100 x 100 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값 구하라
import sys
sys.stdin = open("input.txt")
sys.stdout = open("out.txt","w")

tc = 10
# tc = int(input())

for i in range(tc):
    line_final = []
    row_final=[]
    leftcross_sum = 0
    rightcross_sum = 0

    test_in = []
    input()
    for j in range(100):
        temp = list(map(int, input().split()))
        test_in.append(temp)

    #행의 합의 최대값
    for x in range(0,100):
        line_sum = 0
        for y in range(0, 100):
            line_sum+=test_in[x][y]
        line_final +=[line_sum]


    #열의 합의 최대값
    for y in range(0, 100):
        row_sum = 0
        for x in range(0, 100):
            row_sum+=test_in[x][y]
        row_final +=[row_sum]

    #left_cross 합의 최대값
    for x in range(0, 100):
            leftcross_sum+=test_in[x][x]


    #right_cross 합의 최대값
    for x in range(0, 100):
            rightcross_sum+=test_in[x][-x-1]


    result = max(max(line_final), max(row_final), leftcross_sum, rightcross_sum)

    print('#{} {}'.format(i+1, result))


