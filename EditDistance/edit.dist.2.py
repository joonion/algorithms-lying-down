def mindist(i, j, x, y, A):
    if A[i][j] == -1:
        m, n = len(x), len(y)
        if i == m:
            A[i][j] = 2 * (n - j)
        elif j == n:
            A[i][j] = 2 * (m - i)
        else:
            penalty = 0 if x[i] == y[j] else 1
            A[i][j] = min(mindist(i + 1, j + 1, x, y, A) + penalty,
                          mindist(i + 1, j, x, y, A) + 2,
                          mindist(i, j + 1, x, y, A) + 2)
    return A[i][j]
    
x, y = input(), input()
A = [[-1] * (len(y) + 1) for _ in range(len(x) + 1)]
print(mindist(0, 0, x, y, A))
for i in range(len(A)):
    print(A[i])