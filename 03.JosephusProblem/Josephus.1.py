# Josephus Problem:
#   LeetCode 1823. Find the Winner of the Circular Game

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = [i for i in range(1, n + 1)]
        while len(q) > 1:
            for j in range(1, k + 1):
                friend = q.pop(0)
                if j != k:
                    q.append(friend)
        return q[0]

s = Solution()
print(s.findTheWinner(41, 3))