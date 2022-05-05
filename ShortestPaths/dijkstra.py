# Dijkstra Algorithm

def dijkstra(n, s, W):
    path = [s] * n
    dist = W[s]
    found = [False] * n
    found[s] = True
    # print(path, '\n', dist, '\n', found)

    for _ in range(n - 1):
        minlength = INF
        for i in range(n):
            if not found[i] and dist[i] < minlength:
                minlength = dist[i]
                vnear = i
        found[vnear] = True
        for i in range(n):
            if not found[i] and dist[i] > dist[vnear] + W[vnear][i]:
                dist[i] = dist[vnear] + W[vnear][i]
                path[i] = vnear
        # print(path, '\n', dist, '\n', found)
    return path, dist

INF = 999
n, m = map(int, input().split())
W = [[INF] * n for _ in range(n)]
for i in range(n):
    W[i][i] = 0
for i in range(m):
    u, v, w = map(int, input().split())
    W[u][v] = w
    
path, dist = dijkstra(n, 0, W)
print(path)
print(dist)
