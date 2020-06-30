#내방식 아님
#행 우선, 열 우선, 3x3 사각 영역
def lineCheck():
    for i in range(9):
        # 매 행을 시작할 때 초기화가 필요한 작업
        row = [0] * 10      #1~9
        # 매 열을 시작할 때 초기화가 필요한 작업
        col = [0] * 10
        for j in range(9):
            if row[arr[i][j]] or col[arr[j][i]]:
                return 0
            row[arr[i][j]] = col[arr[j][i]] = 1
    return 1

def rectcheck():
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            rect = [0] * 10
            #왼쪽 모서리 (i,j)에서 높이 = 너비 = 3 사각영역 읽어야 됨
            for x in range(i, i+3):
                for y in range(j, j+3):
                    if rect[arr[x][y]]:
                        return 0
                    rect[arr[x][y]] = 1
    return 1

for tc in range(1, int(input()) + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = lineCheck()+rectcheck()
    if result == 2:
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))