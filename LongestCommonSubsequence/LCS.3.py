def print_matrix(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end = " ")
        print()
        
def lcs(x, y):
    x, y = [' '] + x, [' '] + y
    m, n = len(x), len(y)
    c = [[0 for _ in range(n)] for _ in range(m)]
    b = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            if x[i] == y[j]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = 1
            else:
                c[i][j] = max(c[i][j - 1], c[i - 1][j])
                b[i][j] = 2 if (c[i][j - 1] > c[i - 1][j]) else 3
    return c, b
            
def get_lcs(i, j, b, x):
    if i == 0 or j == 0:
        return ""
    else:
        if b[i][j] == 1:
            return get_lcs(i - 1, j - 1, b, x) + x[i]
        elif b[i][j] == 2:
            return get_lcs(i, j - 1, b, x)
        elif b[i][j] == 3:
            return get_lcs(i - 1, j, b, x)

x = list(input())
y = list(input())
c, b = lcs(x, y)
print_matrix(b)
print(get_lcs(len(x), len(y), b, [' '] + x))
