class Solution:

    def findTargetSumWays(self, nums, S: int) -> int:
        nums_sum = sum(nums)
        if S > nums_sum:
            return 0
        elif (nums_sum+S)%2 != 0:
            return 0
        else:
            half_s = int((nums_sum+S)/2)

        dp = [[0 for _ in range(half_s+1)] for n in nums]
        for row in dp:
            row[0] = 1

        for i, n in enumerate(nums):
            for j in range(half_s+1):
                if n > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-n]

        return dp[-1][-1]


solution = Solution()
opt = solution.findTargetSumWays([1,1,1,1,1], 3)
print(opt)