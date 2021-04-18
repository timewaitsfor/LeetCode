class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        # dp[0] = 1
        for i in range(1, n+1):
            r = 1
            for j in range(1, i):
                r = max(r, dp[i - j]*j, (i-j)*j)
            dp[i] = r
        return dp[n]

solution = Solution()
print(solution.integerBreak(2))