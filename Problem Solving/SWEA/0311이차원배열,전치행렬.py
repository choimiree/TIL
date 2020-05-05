#2차원 배열
#지그재그 순회
for i in range(len(Array)): #i행
    for j in range(len(Array[0])): #j열
        Array[i][j + (m-1-2*j) * (i%2)]
        #필요한 연산 수행

#델타를 이용한 2차 배열의 탐색
    #2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법
arr[0...n-1][0...n-1]
dx[] <- [0,0,-1,1] #상하좌우
dy[] <- [-1,1,0,0]
for x in range(len(arr)):
    for y in range(len(arr[x])):
        for I in range(4):
            testX <- x + dx[mode]
            testY <- y + dy[mode]
            test(arr[testX][testY])

#x:행, y:열
#상,하,좌,우
#dx = [-1,1,0,0]
#dy = [0,0,-1,1]
diff = [(-1,0),(1,0),(0,-1),(0,1)]
arr=[[]]
#행우선으로 모든 위치에 대해 상하좌우 탐색
for x in range(N):
    for y in range(N):
        #상,하,좌,우
        for i in range(4):
            tx, ty = x + dx[i], y + dy[i]
            #항상 경계체크가 필요하다.
            if 0 <= tx < N and 0 <= ty < N:
                # tx, ty에 대해서 작업을 한다.

#전치 행렬
#i: 행의 좌표, len(arr)
#j: 열의 좌표, len(arr[0])
arr = [[1,2,3],[4,5,6],[7,8,9]] #3*3행렬
for i in range(3):
    for j in range(3):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

#부분집합 생성하기
bit = [0,0,0,0]
for i in range(2):
    bit[0] = i  #0번째 원소
    for j in range(2):
        bit[1] = j  #1번째 원소
        for k in range(2):
            bit[2] = k     #2번째 원소
            for n in range(2):
                bit[3] = n      #3번째 원소
                print(bit)       #생성된 부분집합 출력

#보다 간결하게 부분집합을 생성하는 방법
arr = [3,6,7,1,5,4]
n=len(arr)      #n: 원소의 개수
for i in range(1<<n):   #1<<n: 부분집합의 개수
    for j in range(n):    #원소의 수만큼 비트를 비교함
        if i &(1>>j):       #i의 j번째 비트가 1이면 j번째 원소 출력
            print(arr[j], end=", ")
        print()
    print()