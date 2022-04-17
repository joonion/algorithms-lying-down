# Greedy with Iteration

def selection(n, s, f):
    S = []
    F = 0
    for k in range(1, n + 1):
        if F <= s[k]:
            S += [k]
            F = f[k]
    return S

n = int(input())
s, f = [0] * (n + 1), [0] * (n + 1)
for i in range(1, n + 1):
    s[i], f[i] = map(int, input().split())
solution = selection(n, s, f)
print(len(solution), solution)
