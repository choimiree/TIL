# 가로,세로의 크기가 100인 정사각형의 흰색 도화지가 있다.
# 이 도화지 위에 가로,세로의 크기가 각각 10인 정사각형 모양의 검은 색종이를 색종이의 변과 도화지의 변이 평행하도록 붙인다.
# 이러한 방식으로 색종이를 한 장 또는 여러 장 붙인 후 색종이가 붙은 검은 영역의 넓이를 구하는 프로그램을 작성하시오.
# 예를 들어 흰색 도화지 위에 세장의 검은색 색종이를 그림과 같은 모양으로 붙였다면, 검은색 영역의 넓이는 260이 된다.
# [입력]
# 첫째줄에 색종이의 수가 주어진다.
# 한 줄에 하나씩 색종이를 붙인 위치가 주어진다.
N=int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
paper = [[0]*100 for _ in range(100)] # 빈 도화지
for k in range(N):  #색종이 크기만큼 붙이기 반복
    for m in range(arr[k][0], arr[k][0]+10):    #가로10
        for n in range(arr[k][1], arr[k][1]+10):    #세로10
            paper[m][n] = 1                 # 1로 채우기

cnt=0
for i in range(len(paper)):     #색종이가 붙은 칸 세기
    for j in range(len(paper)):
        if paper[i][j] == 1:    #1이면 카운팅
            cnt += 1    #1인 것 다 합쳐줌

print("{}".format(cnt))