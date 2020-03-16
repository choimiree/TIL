##정사각형 방
#N^2개의 방이 NxN 형태로 늘어서 있다.
#위에서 i번째 줄의 왼쪽에서 j번째 방에는 1이상 n^2이하의 수 Ai,j가 적혀 있으며, 이 숫자는 모든 방에 대해 서로 다르다.
#당신이 어떤 방에 있다면, 상하좌우에 있는 다른 방으로 이동할 수 있다.
#물론 이동하려는 방이 존재해야 하고, 이동하려는 방에 적힌 숫자가 현재 방에 적힌 숫자보다 정확히 1 더 커야 한다.
#처음 어떤 수가 적힌 방에서 있어야 가장 많은 개수의 방을 이동할 수 있는지 구하는 프로그램을 작성하라.

di = [0,1,0,1]
dj = [1,0,-1,0]

T= int(input())
for tc in range(1,T+1):
    N=int(input())
    rm = [list(map(int,input().split()))for i in range(N)]
    v = [0]*(N*N+1) #이웃한 칸에 (i칸 옆에 i+1이 있으면) 체크하기 위해
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <=ni< N and 0 <=nj<N and rm[i][j]+1 == rm[ni][nj]:
                    v[rm[i][j]] = 1 #1차이나는 방 표시
    cnt = 0
    maxV = 0
    st = 0 #최대구간의 시작 인덱스
    for i in range(N*N, -1, -1): #오른쪽부터 v[0] 확인
        if v[i]==1: #이웃칸에 i+1이 있는 경우
            cnt += 1 #연속한 1의 개수
        else: #0을 만나면
            if maxV<=cnt: #길이가 같으면 왼쪽 구간 선택
                maxV = cnt #구간의 최대 길이
                st = i+1 #가장 긴 구간의 시작 인덱스
            cnt = 0
    print('#{} {} {}'.format(tc,st,maxV+1))