#Kadane's Algorithm

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum, maxsum = 0, nums[0]
        for i in range(len(nums)):
            cursum = max(cursum + nums[i], nums[i])
            maxsum = max(cursum, maxsum)
            print(i, cursum, maxsum)
        return maxsum

s = Solution()
# n = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]
n = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(s.maxSubArray(n))