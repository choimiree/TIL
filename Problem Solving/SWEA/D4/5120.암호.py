class Node:
    def __init__(self, d=0, p=None, n=None):
        self.data = d
        self.prev = p
        self.next = n

class LinkedList:
    def __init__(self):
        self.head = None
        #self.tail = None
        self.size = 0

def addLast(lst, new):
    if lst.head is None:    #빈 리스트일 경우
        lst.head = new
        new.prev = new.next = new
    else:
        tail = lst.head.prev
        #새로추가되는노드부터
        new.prev = tail
        new.next = lst.head
        tail.next = new
        lst.head.prev = new

    lst.size += 1

def printList(lst):
    if lst.head is None: return
    cur = lst.head
    for _ in range(lst.size):
        print(cur.data, end=' ')
        cur = cur.next
    print()
    cur = lst.head.prev
    for _ in range(lst.size):
        print(cur.data, end=' ')
        cur = cur.prev
    print()

mylist = LinkedList()

arr = [6, 2, 4, 9, 1, 5]
for val in arr:
    addLast(mylist, Node(val))

cur = mylist.head
for _ in range(3):  #M
    for _ in range(3):  #K
        cur = cur.next
    prev = cur.prev
    new = Node(prev.data + cur.data, prev, cur)
    prev.next = new
    cur.next = new  #새로 추가된 위치를 시작위치로 재설정
    mylist.size += 1

printList(mylist)