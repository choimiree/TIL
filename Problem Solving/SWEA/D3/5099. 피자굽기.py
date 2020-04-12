'''
화덕이 queue로 동작하면 된다.
제일 앞에 있는 것이 화덕의 입구.
'''

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    queue = []
    for i in range(N):
        queue.append([C[i], i]) # 먼저 화덕에 피자 채움

    i = 0
    while len(queue) != 1:
        queue[0][0] //= 2 # 처음 피자의 치즈 양을 나눈다.

        if queue[0][0] == 0: # 치즈가 0이라면
            if N+ i < M: # 아직 들어갈 피자가 있다면,
                queue.pop(0) # 처음 피자를 빼고
                queue.append([C[N+i], N+i]) # 다음 피자를 넣는다.
                i += 1
            elif N+i >= M:
                queue.pop(0)
        else: # 치즈가 0이 아니라면, 빼서 뒤로 다시 넣는다.
            queue.append(queue.pop(0))

    print('#{} {}'.format(tc, queue[0][1] + 1))

#2)
def fint():
    pot = queue.Queue()

    for i in range(1, N+1): #화덕에 N개를 채움
        pot.put(i)
    idx = N+1   #아직 화덕에 넣지 않은 피자
    t = 0
    while pot.empty()==False:
        t=pot.get() #입구로 돌아온 피자를 꺼내 치즈 확인
        if arr[t]//2 != 0:  #치즈가 남아있으면
            arr[t] //= 2
            pot.put(t)  #다시 넣고
        elif idx<=M:    #치즈가 녹았으면 남은 피자를 넣음
            pot.put(idx)
            idx += 1
        return t    #마지막으로 나온 피자 번호

T=int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [0]+list(map(int,input().split()))
    print('#{} {}'.format(tc,find()))