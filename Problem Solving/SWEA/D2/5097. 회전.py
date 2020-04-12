#list사용
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))

    for i in range(M):
        num_list.append(num_list[0])
        num_list.pop(0)

    print('#{} {}'.format(tc, num_list[0]))

# 원형 Queue방법
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    front = 0
    rear = 0
    q = [0]+list(map(int,input().split()))
    rear=N
    qlen=N+1
    for _ in range(M):
        front=(front+1)%qlen
        t=q[front]
        rear = (rear+1)%qlen
        q[rear]=t
    print('#{} {}'.format(tc, q[(front+1)%qlen]))
