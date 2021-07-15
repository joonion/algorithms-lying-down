# Josephus Problem:
#   LeetCode 1823. Find the Winner of the Circular Game

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = [i for i in range(1, n + 1)]
        j = 0
        while len(q) > 1:
            j = (j + k - 1) % len(q)
            q.pop(j)
        return q[0]

s = Solution()
print(s.findTheWinner(41, 3))