# 평면에 네개의 직사각형이 놓여 있는데 그 밑변은 모두 가로축에 평행하다.
# 이 네개의 직사각형들은 서로 떨어져 있을 수도 있고, 겹쳐 있을 수도 있고, 하나가 다른 하나를 포함할 수 도 있으며, 변이나 꼭짓점이 겹칠수도 있다.
# 이 직사각형들이 차지하는 면적을 구하라
# c1,r1,c2,r2
pan = [[0]*100 for _ in range(100)]
for _ in range(4):
    x1, y1, x2, y2 = map(int,input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            # print(i, j)
            pan[i][j] = 1
            # print(pan[i][j])
result = 0
for x in range(100):
    for y in range(100):
        if pan[x][y] == 1:
            result += 1
print(result)