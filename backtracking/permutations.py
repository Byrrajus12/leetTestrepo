# Problem: Permutations
# Difficulty: Medium
# Topics: Array, Backtracking
# URL: https://leetcode.com/problems/permutations/
# Submitted At: April 9, 2026 7:09 PM

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums[:]]
        
        res = []

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for p in perms:
                p.append(n)
            
            res.extend(perms)
            nums.append(n)
        
        return res
