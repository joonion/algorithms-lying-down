# Greedy with Recursion

def selection(s, f, k, n):
    m = k + 1
    while m <= n and s[m] < f[k]:
        m = m + 1
    if m > n:
        return []
    else:
        return [m] + selection(s, f, m, n)

n = int(input())
s, f = [0] * (n+1), [0] * (n+1)
for i in range(1, n + 1):
    s[i], f[i] = map(int, input().split())
solution = selection(s, f, 0, n)
print(len(solution), solution)
