class Solution:
    def lastStoneWeightII(self, stones) -> int:
        max_sum = sum(stones)
        dp = [0 for _ in range(max_sum + 1)]
        dp[-1] = 1
        memo = [_ for _ in dp]
        for stone in stones:
            for m in range(2 * stone, max_sum + 1)[::-1]:
                if memo[m] == 1:
                    dp[m - 2 * stone] = 1
            memo = [_ for _ in dp]

        for i, n in enumerate(dp):
            if n == 1:
                return i

solution = Solution()
opt = solution.lastStoneWeightII([75,53,41,71,20,19])
print(opt)
