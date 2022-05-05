def make_graph(n, m):
    imove = [-2, -1, 1, 2,  2,  1, -1, -2]
    jmove = [ 1,  2, 2, 1, -1, -2, -2, -1]
    graph = {i:[] for i in range(n * m)}
    for i in range(n):
        for j in range(m):
            for k in range(8):
                ni, nj = i + imove[k], j + jmove[k]
                if 0 <= ni < n and 0 <= nj < m:
                    graph[i*m + j].append(ni*m + nj)
    return graph

def tour(k, v, s, n, m, graph, mark):
    global count
    if k == n * m and s in graph[v]:
        count += 1
        mark[v] = k
        # for i in range(n):
        #     for j in range(m):
        #         print(f"{mark[i*m + j]:>2d}", end = " ")
        #     print()
    else:
        for u in graph[v]:
            if mark[u] == 0:
                mark[u] = k + 1
                tour(k + 1, u, s, n, m, graph, mark)
                mark[u] = 0

n, m = 3, 10
graph = make_graph(n, m)
for i in range(n * m):
    print(i, ":", graph[i])
mark = [0] * (n * m)

s = 0 # starting vertex
mark[s] = 1 # mark starting vertex
count = 0
tour(1, s, s, n, m, graph, mark)
print(count)
