visit = [0] * N

def possible(k, c):  #k번 퀸의 위치는 (k, c)
    for i in range(k):
        if k-1 == abs(c-col[i]): return False
    return True

def nQueen(k):
    if k == N:
        #카운팅
        pass
    else:
        for i in range(N):
            if visit[i]: continue
            # 퀸들이 서로 대각에 위치하는지 판단
            # k번째 퀸의 열값을 i로 결정
            # 그 이전에 결정한 상태는 0~k-1번까지 결정
            if not possible(k, i): continue
            visit[i] = 1
            col[k]=i
            nQueen(k+1)
            visit[i]=0

for tc in range(1, int(input())+1):
    N = int(input())

    col = [0] * N
    visit = [0] * N
