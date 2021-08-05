



class Solution:
    def maxSubArray(self, nums):
        memo = [0 for n in nums]
        memo[0] = nums[0]
        max_sum = memo[0]
        for i, rn in enumerate(nums[1:]):
            r_idx= i+1
            memo[r_idx] = max(memo[r_idx-1]+rn, rn)
            if memo[r_idx] > max_sum:
                max_sum = memo[r_idx]
        return max_sum



nums = [-2,1,-3,4,-1,2,1,-5,4]

solution = Solution()
opt = solution.maxSubArray(nums)
print(opt)