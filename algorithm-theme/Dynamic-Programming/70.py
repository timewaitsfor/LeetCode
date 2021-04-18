class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1]
        for i in range(1, n+1):
            if i - 2 < 0:
                r = dp[i-1]
            else:
                r = dp[i-1]+dp[i-2]
            dp.append(r)
        return r