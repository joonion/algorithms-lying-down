# Divide-and-Conquer

def selection(i, j, s, f):
    opt = 0
    for k in range(i + 1, j):
        if f[i] <= s[k] and f[k] <= s[j]:
            opt = max(opt, selection(i, k, s, f) + selection(k, j, s, f) + 1)
    return opt

n = int(input())
s, f = [0] * (n+1), [0] * (n+1)
for i in range(1, n + 1):
    s[i], f[i] = map(int, input().split())
s, f = s + [max(f)], f + [max(f)]
solution = selection(0, n + 1, s, f)
print(solution)
