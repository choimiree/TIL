class Node:
    def __init__(self, d=0, p=None, n=None):
        self.data = d
        self.prev = p
        self.next = n

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

def addList(lst, arr):  #리스트를 추가해야할 경우
    first = last = Node(arr[0])
    for val in arr[1:]:
        new = Node(val, last)
        last.next = new #새로운 노드의 첫번째는 기존의 노드 마지막을 가리킴
        last = new  #기존의 노드를 새로운 노드로 바꿔줌

    if lst.head is None:    #빈 리스트일 경우
        lst.head, lst.tail = first, last
    else:
        cur=lst.head
        while cur is not None:
            if cur.data > arr[0]: break
            cur = cur.next
        if cur is None: #삽입할 위치가 뒤쪽
            first.prev = lst.tail
            lst.tail.next = first
            lst.tail =last
        elif cur.prev is None:  #삽입할 위치가 앞에
            last.next = lst.head
            lst.head.prev = last
            lst.head = first
        else:   #삽입할 위치가 중간
            prev = cur.prev
            first.prev = prev
            last.next = cur
            prev.next = first
            cur.prev = last
    lst.size += len(arr)

def printList(lst):
    if lst.head is None: return #항상 빈리스트인지 체크하는 습관 들일 것

    count_10 = 10
    if lst.size < 10:
        count_10 = lst.size

    count = 0
    cur = lst.tail
    while count is not count_10:    #문제풀이에 맞게 변형
        print(cur.data, end=' ')
        cur = cur.prev
        count += 1
    print()

T=int(input())
for tc in range(1, T+1):
    N,M=map(int,input().split())
    # arr = [list(map(int, input().split())) for _ in range(M)]
    mylist = LinkedList()
    for i in range(M):
        addList(mylist, list(map(int,input().split())))

    print('#{}'.format(tc), end=' ')
    printList(mylist)
