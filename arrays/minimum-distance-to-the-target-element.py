# Problem: Minimum Distance to the Target Element
# Difficulty: Easy
# Topics: Array
# URL: https://leetcode.com/problems/minimum-distance-to-the-target-element/
# Submitted At: April 13, 2026 6:50 PM

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        result = len(nums)

        for i in range(len(nums)):
            if nums[i] == target:
                result = min(result, abs(i - start))

        return result
