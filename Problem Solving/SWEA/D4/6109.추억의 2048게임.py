#만약 어떤 타일이 밀리는 방향에 다른 타일이 있고, 두 타일에 적힌 숫자가 같다면 두 타일은 합쳐져 새로운 하나의 타일이 되고, 이 타일에 적힌 숫자는 합쳐진 숫자들의 합이 된다.
#이렇게 합쳐져서 만들어진 새로운 타일은 숫자가 같은 다른 타일이 밀려와도 합쳐져서는 안 된다.
#만약 같은 숫자가 적힌 타일이 세개이상 있을 때는 헷갈리는 경우를 없애기 위해 빨리 벽에 닿게 될 타일을 먼저 민다고 생각한다.
#타일을 모두 이동시키고 나면 격자가 어떻게 변할지 계산하는 프로그램
#입력: 하나의 정수 N(1<=N<=20)과 하나의 문자열 S가 공백 하나로 구분
# S 는 "left" "right" "up" "down"의 넷 중 하나이며 각 타일들은 왼쪽,오른쪽,위쪽,아래쪽으로 이동시키겠따는 뜻.
# N개의 정수들은 0이거나 2이상 1024이하의 2의 제곱수들이다.
# 0이면 이 칸에 타일이 없음을 의미한다.

def f(N, tile):
    ans = [[0]*N for _ in range(N)]
    for r in range(N):
        st = []
        for i in range(N):
            if tile[r][i]!=0:   # 0을 제거
                st.append(tile[r][i])
        i = N-1                 # 오른쪽 칸부터 채움
        while len(st)>=2:        # 2개 이상이면
            a = st.pop()        # 2개의 숫자를 꺼내
            b = st.pop()
            if a==b:            # 두 개가 같으면
                ans[r][i] = a + b # 더해서 넣고
            else:               # 숫자가 다르면
                ans[r][i] = a   # 먼저 꺼낸 숫자를 쓰고
                st.append(b)    # 나중에 꺼낸 숫자는 다시 돌려놓음
            i -= 1              # 왼쪽 칸 채우러 이동
        if st: # 1개 남은 경우
            ans[r][i] = st.pop()    # 남은 숫자로 채움
    return ans

def cw(N, org):
    dest = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            dest[i][j] = org[N-1-j][i]
    return dest


T = int(input())
for tc in range(1, T+1):
    s = list(input().split())
    N = int(s[0])
    S = s[1]
    tile = [list(map(int, input().split())) for i in range(N)]
    ans = []
    if S=='right':
        ans = f(N, tile)
    elif S=='up':
        tile = cw(N, tile)
        ans = f(N, tile)
        for _ in range(3):
            ans = cw(N, ans)
    elif S=='left':
        tile = cw(N, tile)
        tile = cw(N, tile)
        ans = f(N, tile)
        ans = cw(N, ans)
        ans = cw(N, ans)
    elif S=='down':
        for _ in range(3):
            tile = cw(N, tile)
        ans = f(N, tile)
        ans = cw(N, ans)

    print('#{} '.format(tc))
    for i in range(N):
        for j in range(N):
            print(ans[i][j], end=' ')
        print()