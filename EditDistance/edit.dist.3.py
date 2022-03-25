def mindist(x, y):
    m, n = len(x), len(y)
    A = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m):
        A[i][n] = 2 * (m - i)
    for j in range(n):
        A[m][j] = 2 * (n - j)
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            penalty = 0 if x[i] == y[j] else 1
            print(penalty)
            A[i][j] = min(A[i + 1][j + 1] + penalty,
                          A[i + 1][j] + 2,
                          A[i][j + 1] + 2)
    return A
    
x, y = input(), input()
A = mindist(x, y)
for i in range(len(A)):
    print(A[i])