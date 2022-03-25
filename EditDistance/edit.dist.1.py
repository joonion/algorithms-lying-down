def mindist(i, j, x, y):
    m, n = len(x), len(y)
    if i == m:
        return 2 * (n - j)
    elif j == n:
        return 2 * (m - i)
    else:
        penalty = 0 if x[i] == y[j] else 1
        return min(mindist(i + 1, j + 1, x, y) + penalty,
                   mindist(i + 1, j, x, y) + 2,
                   mindist(i, j + 1, x, y) + 2)
    
x, y = input(), input()
print(mindist(0, 0, x, y))
