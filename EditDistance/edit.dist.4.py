def mindist(x, y):
    m, n = len(x), len(y)
    A = [[0] * (n + 1) for _ in range(m + 1)]
    E = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m):
        A[i][n] = 2 * (m - i)
    for j in range(n):
        A[m][j] = 2 * (n - j)
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            penalty = 0 if x[i] == y[j] else 1
            a = A[i + 1][j + 1] + penalty
            b = A[i + 1][j] + 2
            c = A[i][j + 1] + 2
            minvalue = min(a, b, c)
            A[i][j] = minvalue
            E[i][j] = 1 if a == minvalue else \
                      2 if b == minvalue else 3
    return A, E
    
x, y = input(), input()
A, E = mindist(x, y)
for i in range(len(E)):
    print(E[i])