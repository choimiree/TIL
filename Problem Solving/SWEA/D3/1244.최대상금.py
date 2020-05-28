'''
정해진 횟수만큼 숫자판을 교환했을 때 받을 수 있는 가장 큰 금액
#완전검색+가지치기
입력: 숫자판의 정보 + 교환 횟수, 최대자릿수는 6자리, 최대 교환 횟수는 10번
'''

import sys
sys.stdin = open("1244.txt","r")

def SelectionSort(lst,N):
    n=len(lst)
    N2 = 0
    visited = [0]*n
    for i in range(n-1):
        max = i
        for j in range(n-1,i,-1):
            if lst[j] > lst[max]:
                max = j
        if max != i:
            lst[max], lst[i] = lst[i], lst[max]
            visited[max] += 1
            visited[i] += 1
            N2 += 1
        if N == N2:
            if N2 % 2 == 0:
                for k in range(n-1):
                    if visited[k] == 1 and visited[k+1] == 1 and lst[k]<lst[k+1]:
                        lst[k+1], lst[k] = lst[k], lst[k+1]
            return

    if n == len(list(set(lst))):   #숫자 중복이 없는 경우
        for k in range(N-N2):   #크기 배열 완료시 뒤에 두 숫자만 바꾼다.
            lst[-1], lst[-2] = lst[-2], lst[-1]

T=int(input())
for tc in range(1, T+1):
    Number,N=map(str,input().split())
    Number = list(map(int, Number))
    N=int(N)
    if N>10:
        N=10
    SelectionSort(Number, N)
    print('#{} {}'.format(tc, ''.join(map(str,Number))))