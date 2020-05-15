#서로다른 정수 N개가 주어지면 정렬한 상태로 리스트 A에 저장한다.
#정렬한상태로 리스트A에 저장!!
#그런 다음 리스트B에 저장된 M개의 정수에 대해 A에 들어있는 수인지 이진 탐색을 통해 확인하려고 한다.
#전체 탐색 구간의 시작과 끝 인덱스를 l과 r이라고 하면, 중심 원소의 인덱스 m=(l+2)//2이고, 이진 탐색의 왼쪽 구간은 l부터 m-1, 오른쪽 구간은 m+1부터 r이 된다.
#이때 B에 속한 어떤 수가 A에 들어있으면서, 동시에 탐색과정에서 양쪽구간을 번갈아 선택하게 되는 숫자의 개수를 알아보려고 한다.
#A와B에 속한 정수의 개수 N,M이 주어지고, 두 줄에 걸쳐 N개와 M개의 백만 이하의 양의 정수가 주어진다.

#이진탐색:반복으로 풀면됨
import sys
sys.stdin = open("5207input.txt", "r")


def BinarySearch(l, r, nls, x):  # x 는 찾는값
    before = None
    while l <= r:
        m = (l + r) // 2
        if nls[m] == x:
            return True
        elif x > nls[m]:
            l = m + 1
            now = 1
        elif x < nls[m]:
            r = m - 1
            now = -1
        if now == before:
            return False
        before = now

    return False


T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    nls = sorted(list(map(int, input().split())))
    mls = sorted(list(map(int, input().split())))
    result = 0
    for i in range(len(mls)):
        x = mls[i]
        l = 0
        r = len(nls) - 1
        if BinarySearch(l, r, nls, x):
            result += 1

    print('#{} {}'.format(tc, result))