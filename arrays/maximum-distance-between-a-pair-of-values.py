# Problem: Maximum Distance Between a Pair of Values
# Difficulty: Medium
# Topics: Array, Two Pointers, Binary Search
# URL: https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/
# Submitted At: April 19, 2026 4:41 PM

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        ans = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                ans = max(ans, j - i)
                j += 1
            else:
                i += 1
                if i > j:
                    j = i

        return ans
