#트리의 일부를 서브트리라고 한다. 주어진 이진 트리에서 노드 N을 루트로 하는 서브 트리에 속한 노드의 개수를 알아내는 프로그램을 만드시오.
#주어지는 트리는 부모와 자식 노드 번호 사이에 특별한 규칙이 없고, 부모가 없는 노드가 전체의 루트 노드가 된다.
#이런 경우의 트리는 부모 노드를 인덱스로 다음과 같은 방법으로 나타낼 수 있다. 자식 노드가 0인 경우는 노드가 자식이 없는 경우이다.
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class Tree:
    def __init__(self, cnt):
        self.node_lst = [None]
        for i in range(E + 1):
            self.node_lst.append(Node(i))

    def put(self, parent, child):
        if self.node_lst[parent].left == None:
            self.node_lst[parent].left = self.node_lst[child]
        else:
            self.node_lst[parent].right = self.node_lst[child]

    def count(self, node):
        self.cnt += 1
        if node.left != None:
            self.count(node.left)
        if node.right != None:
            self.count(node.right)

    def result(self, num):
        self.cnt = 0
        self.count(self.node_lst[num])
        return self.cnt


T = int(input())
for t in range(1, T+1):
    E, N = map(int, input().split())
    put_list = list(map(int, input().split()))
    tree = Tree(E)
    for i in range(E):
        tree.put(put_list[2 * i], put_list[2 * i + 1])
    print('#{} {}'.format(t, tree.result(N)))