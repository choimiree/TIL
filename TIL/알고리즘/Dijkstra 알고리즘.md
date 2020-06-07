# Dijkstra 알고리즘

```python
s: 시작 정점, A: 인접 행렬(그래프) D: 거리(가중치)
V: 정점 집합, U: 선택된 정점 집합
         
Dijkstra(s, A, D)
	U = {s};
    
    for 모든 정점 v
    	D[v] <- A[s][v]
        
    while U != V
    	D[w]가 최소인 정점 w 오른쪽포함 V-U 를 선택
        U <- U U {w}
        
        for w에 인접한 모든 정점 v
        	D[v] <- min(D[v], D[w] + A[w][v])
```

```python
V,E = map(int,input().split())
adj = {i:[] for i in range(V)}
for i in range(E):
    s, e, c = map(int,input().split())
    adj[s].append([e,c])
    
INF = float('inf')
dist = [INF]*V
selected = [False]*V

dist[0] = 0	#시작점을 0으로
cnt = 0

while cnt < V:
    minval = INF
    u = -1
    for i in range(V):
        if not selected[i] and dist[i] <minval:
            minval = dist[i]
            u = i
            
    selected[u] = True
    cnt += 1
    for w,c in adj[u]:
        dist[w] = min(dist[w], dist[u]+c)
        
print(dist)
```

