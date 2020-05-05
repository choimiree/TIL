##Sum
#100x100 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램을 작성하여라.

T = 10
for tc in range(1, 11):

    N = int(input())
    pan = [list(map(int, input().split())) for _ in range(100)]

    result = []
    leftcross = 0 #왼쪽위에서 오른쪽 아래로 내려가는 대각선 합
    rightcross = 0 #우른쪽위에서 왼쪽 아래로 내려가는 대각선 합

    for i in range(0, 100):
        linesum = 0 #행의 합은 행이 바뀔 때마다 초기화
        for j in range(0, 100):
            linesum += pan[i][j]
            result.append(linesum)

    for j in range(0, 100):
        rowsum = 0 #열의 합도 열이 바뀔 때마다 초기화
        for i in range(0, 100):
            rowsum += pan[i][j]
            result.append(rowsum)

    for i in range(0, 100):
        leftcross += pan[i][i]
        result.append(leftcross)

    for i in range(0, 100):
        rightcross += pan[i][-i-1]
        result.append(rightcross)

#   result = linesum + rowsum + leftcross + rightcross
    print('#{} {}'.format(tc, max(result)))
