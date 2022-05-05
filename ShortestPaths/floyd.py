# Floyd Algorithm

def floyd(n, W):
    path = [[-1] * n for _ in range(n)]
    dist = W
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    path[i][j] = k
    return path, dist                    

INF = 999
n, m = map(int, input().split())
W = [[INF] * n for _ in range(n)]
for i in range(n):
    W[i][i] = 0
for i in range(m):
    u, v, w = map(int, input().split())
    W[u][v] = w
    
path, dist = floyd(n, W)
for i in range(n):
    print(dist[i])
print()
for i in range(n):
    print(path[i])
