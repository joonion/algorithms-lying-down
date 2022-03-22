def rodcut(n, p, r):
    if r[n] < 0:
        if n == 0:
            r[n] = 0
        else:
            r[n] = -1
            for i in range(1, n + 1):
                r[n] = max(r[n], p[i] + rodcut(n - i, p, r))
    return r[n]

m = int(input())
p = [0] + list(map(int, input().split()))
n = int(input())
r = [-1] * (n + 1)
print(rodcut(n, p, r))