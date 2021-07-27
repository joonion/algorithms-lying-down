#Kadane's Algorithm

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum, maxsum = 0, nums[0]
        for i in range(len(nums)):
            cursum = max(cursum + nums[i], nums[i])
            maxsum = max(cursum, maxsum)
        return maxsum

s = Solution()
n = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]
print(s.maxSubArray(n))