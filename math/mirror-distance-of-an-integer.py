# Problem: Mirror Distance of an Integer
# Difficulty: Easy
# Topics: Math
# URL: https://leetcode.com/problems/mirror-distance-of-an-integer/
# Submitted At: April 18, 2026 7:17 PM

class Solution:
    def revnum(self, a: int) -> int:
        if a // 10 == 0:
            return a
        return int(str(a)[::-1])

    def mirrorDistance(self, n: int) -> int:
        return abs(n - self.revnum(n))
