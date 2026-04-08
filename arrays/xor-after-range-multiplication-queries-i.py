# Problem: XOR After Range Multiplication Queries I
# Difficulty: Medium
# Topics: Array, Divide And Conquer, Simulation
# URL: https://leetcode.com/problems/xor-after-range-multiplication-queries-i/
# Submitted At: April 8, 2026 3:57 PM

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod = 1000000007

        # Process each query
        for t in queries:
            l = t[0]
            r = t[1]
            k = t[2]
            v = t[3]

            idx = l

            # Apply operation at step k
            while idx <= r:
                temp = nums[idx]
                nums[idx] = (temp * v) % mod
                idx += k

        # Compute XOR of final array
        ans = 0
        for num in nums:
            ans ^= num

        return ans
