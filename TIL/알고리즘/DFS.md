# DFS

```python
def dfs(v):
    visited[v]=1
    print(v, end=" ")
    
    for w in range(1, V+1):
        if G[v][w] == 1 and visited[w] == 0:
            dfs(w)
            
V=7
G=[[0,0,0,0,0,0,0],
  [0,0,1,1,0,0,0],
  ...]
visited = [0] * (V+1)
dfs(1)
```

