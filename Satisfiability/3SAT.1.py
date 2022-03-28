def satisfiable(n, m, b):
    for v in range(2**n):
        for i in range(m):
            t = v
            for j in range(n):
                if b[i][j] == 0:
                    t ^= (1 << (n - j - 1))
            if t == 0:
                return True, v
    return False, None

n, m = map(int, input().split())
b = []
for i in range(m):
    b.append(list(map(int, input().split())))
result, solution = satisfiable(n, m, b)
print("Satisfiable:", result)
if result:
    for i in range(n):
        print(solution & 1, end = " ")
        solution >>= 1
        
   