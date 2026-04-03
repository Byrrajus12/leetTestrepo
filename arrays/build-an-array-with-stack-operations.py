# Problem: Build an Array With Stack Operations
# Difficulty: Medium
# Topics: Array, Stack, Simulation
# URL: https://leetcode.com/problems/build-an-array-with-stack-operations/
# Submitted At: April 3, 2026 7:08 PM

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        curr = 0
        out = []
        for num in range(1, target[-1] + 1):
            if num == target[curr]:
                out.append("Push")
                curr += 1
            else:
                out.append("Push")
                out.append("Pop")
        return out
