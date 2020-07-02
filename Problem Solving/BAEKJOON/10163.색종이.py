#보이는 부분 면적을 구하라
#색종이 장수 N
N=int(input())
#빈정렬
pan=[[0]*101 for _ in range(101)]
#번호 y, x, 너비, 높이
for n in range(1, N+1):
    y, x, w, h = map(int,input().split())
    for i in range(y, y+w):
        for j in range(x, x+h):
            pan[i][j] = n
            # print(pan[i][j])

for n in range(1, N+1):
    result = 0
    for x in range(101):
        for y in range(101):
            if pan[x][y] == n:
                result += 1
    print(result)