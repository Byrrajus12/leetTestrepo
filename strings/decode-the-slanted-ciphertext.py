# Problem: Decode the Slanted Ciphertext
# Difficulty: Medium
# Topics: String, Simulation
# URL: https://leetcode.com/problems/decode-the-slanted-ciphertext/
# Submitted At: April 18, 2026 7:22 PM

class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if not encodedText:
            return encodedText

        cols = math.ceil(len(encodedText) / rows)
        res = []

        for start in range(cols):
            r, c = 0, start
            while r < rows and c < cols:
                res.append(encodedText[r * cols + c])
                r += 1
                c += 1

        return ''.join(res).rstrip()
