# Dynamic Programming

def selection(n, s, f):
    C = [[0] * (n+2) for _ in range(n+2)]
    for i in range(1, n + 1):
        C[i][i] = 1
    for d in range(1, n + 1):
        for i in range(n - d + 1):
            j = i + d
            for k in range(i, j + 1):
                if f[i] <= s[k] and f[k] <= s[j]:
                    C[i][j] = max(C[i][j], C[i][k] + C[k][j] + 1)
    return C

n = int(input())
s, f = [0] * (n+1), [0] * (n+1)
for i in range(1, n + 1):
    s[i], f[i] = map(int, input().split())
C = selection(n, s, f)
for i in range(n + 1):
    for j in range(n + 1):
        print(C[i][j], end=" ")
    print()
print(C[0][n])
