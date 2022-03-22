def rodcut(n, p):
    if n == 0:
        return 0
    else:
        r = -1
        for i in range(1, n + 1):
            r = max(r, p[i] + rodcut(n - i, p))
        return r

m = int(input())
p = [0] + list(map(int, input().split()))
n = int(input())
print(rodcut(n, p))