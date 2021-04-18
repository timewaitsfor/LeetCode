class Solution:
    def canPartition(self, nums) -> bool:
        total_sum = sum(nums)
        if total_sum%2!=0:
            return False
        half_sum = int(total_sum/2)
        dp = [0 for _ in range(half_sum+1)]
        dp[0] = 1
        memo = [_ for _ in dp]
        for i, n in enumerate(nums):
            if n > half_sum:
                return False
            elif n == half_sum:
                return True
            for j in range(0, half_sum-n+1):
                if memo[j] != 0:
                    dp[j+n] = 1
            memo = [_ for _ in dp]

        if dp[-1] == 1:
            return True
        else:
            return False

solution = Solution()
print(solution.canPartition([2,2,3,5]))