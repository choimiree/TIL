#mst prim알고리즘
import heapq

def cost(s1, s2):
    return ratio*((s1[0] - s2[0])**2 + (s1[1] - s2[1])**2)

infinite = float('inf')

for tc in range(1, int(input())+1):
    s_cnt = int(input())
    x_arr = list(map(int,input().split()))
    y_arr = list(map(int,input().split()))
    ratio = float(input())

    arr = [[] for _ in range(s_cnt)]

    for i in range(s_cnt):
        arr[i] = [x_arr[i], y_arr[i]]

    e_cost = [infinite]*s_cnt
    min_tree = [False]*s_cnt
    priority_line = []

    e_cost[0] = 0

    heapq.heappush(priority_line, (0,0))
    result=0
    while priority_line:
        ans, now = heapq.heappop(priority_line)
        if min_tree[now]: continue

        min_tree[now] = True
        result += ans

        for next in range(len(arr)):
            if not min_tree[next] and e_cost[next] > cost(arr[now], arr[next]):
                e_cost[next] = cost(arr[now], arr[next])
                heapq.heappush(priority_line, (e_cost[next], next))

    print('#{} {}'.format(tc, round(result)))
