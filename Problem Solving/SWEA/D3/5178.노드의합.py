#완전이진트리의 리프 노드에 1000이하의 자연수가 저장되어 있고, 리프 노드를 제외한 노드에는 자식 노드에 저장된 값의 합이 들어있다고 한다.
#다음은 리프 노드에 저장된 1,2,3이 주어졌을 때, 나머지 노드에 자식 노드의 합을 저장한 예이다.
#N개의 노드를 갖는 완전 이진 트리의 노드 번호는 루트가 1번이 되며, 같은 단계에서는 왼쪽에서 오른쪽으로 증가, 단계가 꽉 차면 다음단계의 왼쪽부터 시작된다.
def binary_tree(L, tree):
    if L > (len(tree)-1): return 0
    return tree[L] if tree[L] != 0 else binary_tree(L * 2, tree) + binary_tree(L*2 + 1, tree)

for tc in range(int(input())):
    N,M,L = map(int, input().split())
    tree = [0] * (N+1)
    for _ in range(M):
        x, y = map(int,input().split())
        tree[x] = y
    result = binary_tree(L, tree)
    print('#{} {}'.format(tc+1, result))