#NxN칸에 숫자가 적힌 판이 주어지고, 각 칸에서는 오른쪽이나 아래로만 이동할 수 잇다.
#맨왼쪽위에서 오른쪽 아래까지 이동할 때, 지나는 칸에 써진 숫자의 합계가 최소가 되도록 움직였다면, 이때의 합계가 얼마인지 출력하는 프로그램을 만드시오.
#가능한 모든 경로에 대해 합을 계산한 후 최소값을 찾아도 된다.

# 재귀
import sys
sys.stdin = open("5188.txt", "r")

def find(r, c, s):
    global minV
    if r == N - 1 and c == N - 1:  # 목적지 도착
        if minV > s + m[r][c]:
            minV = s + m[r][c]
    elif minV <= s:  # 목적지 도착전에 이미 다른 최소값이 커지면,
        return  # 이동을 중단하고 다른 경로로
    else:
        if r + 1 < N:  # 아래로 이동 가능한지 확인
            find(r + 1, c, s + m[r][c])
        if c + 1 < N:  # 오른쪽으로 이동
            find(r, c + 1, s + m[r][c])

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    m = [list(map(int, input().split())) for i in range(N)]
    minV = 100000  # 최소값 초기화
    find(0, 0, 0)
    print('#{} {}'.format(tc, minV))