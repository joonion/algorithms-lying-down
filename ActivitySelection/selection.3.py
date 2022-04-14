# Divide-and-Conquer

def selection(i, j, s, f):
    if f[i] > s[j]:
        return 0
    else:
        opt = 2
        for k in range(i + 1, j):
            if f[i] <= s[k] and f[k] <= s[j]:
                opt = max(opt, selection(i, k, s, f) + selection(k, j, s, f) + 1)
        return opt

n = int(input())
s, f = [0] * (n+1), [0] * (n+1)
for i in range(1, n + 1):
    s[i], f[i] = map(int, input().split())
solution = selection(1, n, s, f)
print(solution)
