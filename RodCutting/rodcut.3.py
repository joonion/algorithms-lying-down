def rodcut(n, p):
    r = [0] * (n + 1)
    for i in range(1, n + 1):
        r[i] = -1
        for j in range(1, i + 1):
            r[i] = max(r[i], r[i - j] + p[j])
    return r[n]

m = int(input())
p = [0] + list(map(int, input().split()))
n = int(input())
print(rodcut(n, p))