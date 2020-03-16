import sys
sys.stdin = open("0229.txt", "r")

T=int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    

    #선택행렬로 출력
    #print()