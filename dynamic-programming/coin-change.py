# Problem: Coin Change
# Difficulty: Medium
# Topics: Array, Dynamic Programming, Breadth First Search
# URL: https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        # for each amount from 1 to our amount
        for amt in range(1, amount+1):
            # we want to go through each coin and see how it helps and how many at minimum we need to get that amount
            # if the diff b/w amt and the certain coin is >= 0 then we store that value
            # each dp value tells us how much we need to form that value
            # so if the diff is >= 0 we update dp
            # dp[i] = min (dp[i], 1 coin that we're using now + dp[amt - coin] this is so that we use that coin and get the number of coins needed for the rest)
            for coin in coins:
                if amt - coin >= 0:
                    dp[amt] = min(dp[amt], 1 + dp[amt - coin])
        print(dp[amount])
        return dp[amount] if dp[amount] != (amount+1) else -1
