#2016년 삼성전자가 러시아 현지법인을 설립한지 20주년이 된 해이다. 이를 기념해서 당신은 러시아 국기를 만들기로 했따.
#먼저 창고에서 오래된 깃발을 꺼내왔다. 이 깃발은 N행 M열로 나뉘어 있고, 각 칸은 흰색, 파란색, 빨간색 중 하나로 칠해져 있따.
#당신은 몇 개의 칸에 있는 색을 다시 칠해서 이 깃발을 러시아 국기처럼 만들려고 한다. 다음의 조건을 만족해야 한다.
#위에서 몇 줄(한 줄 이상)은 모두 흰색으로 칠해져 있어야 한다.
#다음 몇 줄(한 줄 이상)은 모두 파란색으로 칠해져 있어야 한다.
#나머지 줄(한 줄 이상)은 모두 빨간색으로 칠해져 있어야 한다.
#이렇게 러시아 국기 같은 깃발을 만들기 위해서 새로 칠해야 하는 칸의 개수의  최솟값을 구하여라.
for tc in range(1, int(input())+1):
    N,M = map(int,input().split()) #국기의 크기
    arr = [input() for _ in range(N)] #오래된 국기의 색 정보
    # arr = [1,2,3,4,5]; N = len(arr)
    #4분할은 4C2=6가지 출력
    ans = N*M #모든 칸을 색칠하는 것이 나올수있는 가장 큰 값
    # N-1C2 반복 = (N(N-1))/2
    for i in range(0, N-3+1):
        for j in range(i+1, N-2+1):
            cnt = 0
            #NxM 반복 = 50x50
            #흰색 영역: 0~i까지(행의 범위)
            for r in range(0,i+1):
                for c in range(M):
                    if arr[r][c] != 'W': cnt += 1 #흰색이 아닌거 카운팅
            # print(arr[:i + 1], end='')
            #파란색 영역: i+1~j까지
            for r in range(i+1, j+1):
                for c in range(M):
                    if arr[r][c] != 'B': cnt += 1 #파란색 아닌거 카운팅
            # print(arr[i+1:j+1],end='')
            #빨간색: j+1, N-1까지
            for r in range(j+1, N):
                for c in range(M):
                    if arr[r][c] != 'R': cnt += 1 #빨간색 아닌거 카운팅
            # print(arr[j+1:N],end='')
            # print()
            ans = min(ans,cnt)

#카운팅을 반복적으로 하고 있으니까 효율적으로 하는 방법 => 누적합 사용
#카운팅 값을 누적한 것처럼, 어떤 배열에 정수값이 배열돼있을 때, 정수값의 누적합을 계산해서 구간합을 사용.
#구간합을 구할 때 매번 탐색할 필요없이 빠르게 계산 가능
for tc in range(1, int(input())+1):
    N,M = map(int,input().split()) #국기의 크기
    arr = [input() for _ in range(N)] #오래된 국기의 색 정보

    w = [0] * N
    b = [0] * N
    r = [0] * N
    for i in range(N):
        w[i] = arr[i].count('W')
        b[i] = arr[i].count('B')
        r[i] = M - w[i] - b[i]

    for i in range(1, N):
        w[i] += w[i-1]
        b[i] += b[i-1]
        r[i] += r[i-1]

    ans = N * M
    for i in range(0, N - 3 + 1):
        for j in range(i + 1, N - 2 + 1):
            # 흰 색이 아닌 칸수 = 전체 칸수 - 흰색 수
            cnt = M * (i + 1) - w[i]
            # 두 번째 영역: i+1 ~ j
            cnt += M * (j - (i + 1) + 1) - (b[j] - b[i])
            # 세 번째 영역
            cnt += M * (N - 1 - j) - (r[N - 1] - r[j])

            ans = min(ans, cnt)

