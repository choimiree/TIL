'''
회사에서 출발하여 N명의 고객을 모두 방문하고 집으로 돌아가는 경로중 가장 짧은 것을 찾으려 한다.
가장 짧은 경로를 '효율적으로 찾는 것'이 목적이 아니다.
모든 가능한 경로를 살펴서 해를 찾아도 좋다 #완전검색+가지치기
[제약]
회사의 좌표, 집의 좌표를 포함한 모든 N*2개의 좌표는 서로 다른 위치에 있으며 좌표의 값은 0이상100이하의 정수로 이뤄진다.
[입력]
첫째줄에는 고객의 수 N
둘째줄에는 회사의 좌표, 집의좌표, N명의 고객의 좌표.
좌표는 (x,y) 쌍으로 구성되는데 입력에서는 x와 y가 공백으로..
#순열
'''
import sys
sys.stdin = open("1247.txt","r")

def findway(bx, by, c,s):
    global minway
    if s > minway:
        return
    if c == L-1:
        for i in range(L):
            if V[i] == 0:
                x,y = my_lst[i]
                s += abs(bx-x)+abs(by-y)
                s += abs(x-company[0])+abs(y-company[1])
                break
        if minway > s:
            minway = s
        return
    else:
        for i in range(L):
            if V[i] == 0:
                V[i] = 1
                x,y = my_lst[i]
                findway(x,y,c+1,s+abs(bx-x)+abs(by-y))
                V[i] = 0

T=int(input())
for tc in range(1, T+1):
    N=int(input())
    zapyo_lst=list(map(int,input().split()))
    my_lst = []
    for n in range(N):
        my_lst.append([zapyo_lst[2*(n+2)],zapyo_lst[(2*(n+2))+1]])
    home = [zapyo_lst[0],zapyo_lst[1]]
    company = [zapyo_lst[2], zapyo_lst[3]]
    minway = 100000
    L = len(my_lst)
    V = [0]*L
    findway(home[0], home[1], 0, 0)
    print('#{} {}'.format(tc, minway))
