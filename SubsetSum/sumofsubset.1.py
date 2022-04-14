def sumofsubset(i, W, S, R):
    if W == 0:
        for i in R:
            print(S[i], end=" ")
        return True
    if i < 0 and W != 0:
        return False
    else:
        R.append(i)
        left = sumofsubset(i - 1, W - S[i], S, R)
        R.remove(i)
        right = sumofsubset(i - 1, W, S, R)
        return left or right
    
n, m = map(int, input().split())
S = list(map(int, input().split()))
R = []
for _ in range(m):
    W = int(input())
    print(sumofsubset(n - 1, W, S, R))
