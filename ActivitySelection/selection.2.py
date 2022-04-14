# Greedy with Iteration

def selection(s, f):
    n = len(s) - 1
    S = [1]
    k = 1
    for m in range(2, n + 1):
        if s[m] >= f[k]:
            S += [m]
            k = m
    return S

n = int(input())
s, f = [0] * (n+1), [0] * (n+1)
for i in range(1, n + 1):
    s[i], f[i] = map(int, input().split())
solution = selection(s, f)
print(len(solution), solution)
