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

def tour(k, v, n, m, graph, mark):
    global count
    if k == n * m:
        count += 1
        mark[v] = k
        print(f"solution #{count}:")
        for i in range(n):
            for j in range(m):
                print(f"{mark[i*m + j]:>2d}", end = " ")
            print()
    else:
        for u in graph[v]:
            if mark[u] == 0:
                mark[u] = k + 1
                tour(k + 1, u, n, m, graph, mark)
                mark[u] = 0

n, m = 3, 4
graph = make_graph(n, m)
for i in range(n * m):
    print(i, ":", graph[i])

total = 0
for s in range(n * m):
    mark = [0] * (n * m)
    mark[s] = 1
    count = 0
    tour(1, s, n, m, graph, mark)
    if count > 0:
        print(s, ":", count)
    total += count
print(f"total = {total}")