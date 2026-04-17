# Problem: Minimum Absolute Distance Between Mirror Pairs
# Difficulty: Medium
# Topics: Array, Hash Table, Math
# URL: https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/
# Submitted At: April 17, 2026 7:05 PM

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverseNum(x):
            rev = 0
            while x > 0:
                rev = rev * 10 + x % 10
                x //= 10
            return rev

        mp = {}
        ans = float('inf')

        for j in range(len(nums)):
            if nums[j] in mp:
                ans = min(ans, j - mp[nums[j]])

            rev = reverseNum(nums[j])
            mp[rev] = j

        return -1 if ans == float('inf') else ans
