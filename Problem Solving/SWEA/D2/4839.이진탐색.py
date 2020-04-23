'''
def binarySearch(lo, hi, key):
    if lo > hi: return
    mid = (lo + hi) >> 1 #비트표현
    if mid == key:
        return
    elif mid> key: #왼쪽에서 탐색
        binarySearch(lo, mid, key) + 1
    else:
        binarySearch(mid, hi, key) + 1
for tc in range(1, int(input())+1):
    p, pa, pb = map(int, input().split())
    A = binarySearch(1,p,pa)
    B = binarySearch(1,p,pb)
print('#{} {}'.format(tc, return))
'''
def makeT(n):
    global idx
    global N
    if n <= N:
        makeT(n*2)  #왼쪽 서브트리 방문
        tree[n] = idx   #중위 순회로 현재 노드값 저장
        idx += 1
        makeT(n*2+1)    #오른쪽 서브트리 방문

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    idx = 1
    tree = [0 for i in range(N+1)]  #리스트를 이용한 완전 이진트리 저장
    makeT(1)
    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))
