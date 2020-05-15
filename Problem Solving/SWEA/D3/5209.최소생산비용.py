#A사는 여러곳에 공장을 갖고 있다.
#봄부터 새로 생산되는 N종의 제품을 N곳의 공장에서 한 곳당 한 가지씩 생산하려 한다.
#각제품의 공장별 생산비용이 주어질 때 전체 제품의 최소생산비용을 계산하라.
import sys
sys.stdin=open("5209input.txt","r")

def backtrack(k,result):
    global min_result

    if k == N:
        if min_result > result:
            min_result = result
        return

    if result > min_result:
        return

    else:
        for i in range(N):
            if visited[i] == 0:
                    visited[i] = 1
                backtrack(k+1, result+V[k][i])
                visited[i] = 0


T=int(input())
for tc in range(1,T+1):
    N=int(input())
    V=[list(map(int,input().split())) for _ in range(N)]
    visited = [0]*N
    min_result =  100000
    backtrack(0,0)
    print('#{} {}'.format(tc, min_result))