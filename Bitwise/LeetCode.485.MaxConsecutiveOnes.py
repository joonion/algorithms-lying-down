from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = int("".join(map(str, nums)), 2)
        count = 0
        while n != 0:
            n &= (n << 1)
            count += 1
        return count

sol = Solution()
lin = [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1]
print(sol.findMaxConsecutiveOnes(lin))
       