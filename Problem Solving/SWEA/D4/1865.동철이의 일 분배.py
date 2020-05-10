#동철이가 차린 전자회사에는 N명의 직원이 있다.
#그런데 어느날 해야할 일이 N개가 생겼다.
#동철이는 직원들에게 공평하게 일을 하나씩 배분하려고 한다.
#직원들의 번호가 1부터 N까지 매겨져 있고, 해야 할 일에도 번호가 1부터 N까지 매겨져 있을 때, i번 직원이 j번 일을 하면 성공할 확률이 Pi,j이다.
#여기서 우리는 동철이가 모든 일이 잘 풀리도록 도와주어야 한다.
#직원들에게 해야 할 일을 하나씩 배분하는 방법은 여러 가지이다.
#우리는 여러 방법 중에서 생길 수 있는 "주어진 일이 모두 성공할 확률"의 최댓값을 구하는 프로그램을 작성해야 한다.
def end_work(k, sum):
    global my_max
    if sum == 0 or sum <= my_max:
        return
    if k == N:
        # if my_max <= sum:
        my_max = sum
        return
    for i in range(N): #i == 사람번호
        if man[i] == 0:
            man[i] = 1 #이 사람 이미 일 끝냄
            end_work(k+1, sum*arr[i][k]/100) #k=0 첫 일
            man[i] = 0

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    my_max = 0
    man = [0] * N #visited와 같은 역할
    end_work(0,1)
    print('#{} {:.6f}'.format(tc, my_max*100))

'''
def f(n,k,s): #s는 성공할 확률
    global maxV
    global u
    global w
    global arr
    if n == k:
        if maxV < s*100:
            maxV = s*100
    elif maxV >= s*100:
        return
    else:
        for i in range(k):
            if u[i] == 0:
                u[i] = 1 #i번 사람이 n번 일을 맡음
                f(n+1, k, s*arr[i][n]/100) #n번까지의 성공확률 계산
                u[i] = 0 #다른 일을 맡도록 함
                #확률은 항상 1보다 작으므로 곱할수록 계속 작아진다. 즉 Sn >= Sn+1을 항상 만족한다.(n+1번째 확률이 1이면 Sn = Sn+1)

T=int(input())
for tc in range(1, T+1):
    N=int(input())
    arr = [list(map(int,input().split())) for _ in range(N)] # Pi,j는 i번 사람이 j번 일을 성공할 확률을 퍼센트 단위로 나타낸다.
    u = [0]*N  #일을 맡은 사람을 표시하는 배열 u
    w = [0]*N  #선택한 숫자를 기록할 배열?
    maxV = 0
    f(0,N,1) #1은 성공확률
    print('#{} {:.6f}'.format(tc,maxV))
'''