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
