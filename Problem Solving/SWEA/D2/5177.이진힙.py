def eng(n):
    global last
    last += 1   #마지막 노드번호 증가
    c = last    #마지막 노드를 자식 노드로
    p = c//2    #부모 노드 번호 계산
    q[last] = n #마지막 노드에 가 ㅄ 저장
    while c>1 and q[p] > q[c]:  #루트가 아니고, 부모 노드의 값이 더 크면
        t = q[p]    #저장된 값 바꿈
        q[p] = q[c]
        q[c] = t
        c = p   #부모를 새로운 자식 노드로
        p = p//2

def find(): #마지막 노드의 조상 노드 찾기
    global N
    c = N
    p = c//2
    s = 0
    while p>0:
        s += q[p]   #조상 노드 값을 더함
        p = p//2
    return s

for tc in range(1, T+1):
    N = int(input())
    last = 0    #노드가 하나도 없는 상태
    q = [0 for i in range(N+1)] #이진 힙 구현을 위한 리스트 생성
    l = list(map(int, input().split()))

    for i in range(N):  #힙에 저장
        enq(l[i])
    print('#{} {}'.format(tc, find()))