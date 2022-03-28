def satisfiable(n, m, b):
    for i in range(2**n):
        print(i)
        for j in range(m):
            v = str(bin(i)[2:])
            for k in range(n):
                if b[j][k] == "0":
                    v[i] = "0" if v[i] == "1" else "1"
            if sum(list(map(int, v))) == 0:
                return Fa, str(bin(i)[2:])
    return False, None

n, m = map(int, input().split())
b = []
for i in range(m):
    b.append(list(map(int, input().split())))
result, solution = satisfiable(n, m, b)
print("Satisfiable:", result, solution)
   