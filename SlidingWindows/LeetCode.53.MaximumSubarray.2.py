#Kadane's Algorithm

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cumulate = nums[:]
        for i in range(1, len(nums)):
            cumulate[i] += cumulate[i - 1]
        maxsum = nums[0]
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                cursum = cumulate[j] if i == 0 else \
                         cumulate[j] - cumulate[i - 1]
                maxsum = max(maxsum, cursum)
        return maxsum

s = Solution()
n = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]
print(s.maxSubArray(n))
