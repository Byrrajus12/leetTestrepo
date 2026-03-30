# Problem: House Robber
# Difficulty: Medium
# Topics: Array, Dynamic Programming
# URL: https://leetcode.com/problems/house-robber/
# Submitted At: March 30, 2026 6:17 PM

class Solution:
    def rob(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return nums[0]
        # dp = [0] * len(nums)
        # dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        # for i in range(2, len(nums)):
        #     dp[i] = max(dp[i-1], nums[i]+ dp[i-2])
        # return dp[-1]

        prev = curr = 0

        for num in nums:
            tmp = max(prev + num, curr)
            prev = curr
            curr = tmp
        
        return curr
