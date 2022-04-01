from ntpath import join


INF = 99999

def minimum(i, j, d, M):
    minv, mink = INF, -1
    for k in range(i, j):
        v = M[i][k] + M[k+1][j] + d[i-1]*d[k]*d[j]
        if v < minv:
            minv, mink = v, k
    return minv, mink
    
def chained(n, d):
    M = [[0] * (n + 1) for _ in range(n + 1)]
    P = [[0] * (n + 1) for _ in range(n + 1)]
    for k in range(1, n):
        for i in range(1, n - k + 1):
            j = i + k
            M[i][j], P[i][j] = minimum(i, j, d, M)
    return M, P

def order(i, j, P):
    if i == j:
        return "(" + str(i) + ")"
    else:
        return "(" + \
               order(i, P[i][j], P) + \
               order(P[i][j] + 1, j, P) + \
               ")"
        
def print_matrix(M):
    for i in range(1, len(M)):
        for j in range(i, len(M[i])):
            if j < len(M[i]) - 1:
                print(M[i][j], end=" ")
            else:
                print(M[i][j])
        
n = int(input())
d = list(map(int, input().split()))
M, P = chained(n, d)
print_matrix(M)
print_matrix(P)
print(order(1, n, P))
