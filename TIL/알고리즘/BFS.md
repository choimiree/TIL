# BFS

```python
def bfs(V):
    q=[]
    q.append(v)
    visited[v]=1
    print(v,end=" ")
    while q:
        v=q.pop(0)
        for w in G[v]:
            if not visited[w]:
                q.append(w)
                visited[w]=visited[v]+1
                print(w, end=" ")
                
G = [[], [2,3],[1,4,5],[1,7][2,6],[2,6],[4,5,7],[3,6]]
visitied=[0]*8
bfs(1)

```

