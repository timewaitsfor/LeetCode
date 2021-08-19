class Solution:
    def majorityElement(self, nums) -> int:

        length = len(nums)
        count_dict = {}
        for n in nums:
            this_count = count_dict.get(n, 0)
            count_dict[n] = this_count + 1
            if this_count > length//2:
                return n

solution = Solution()

s =  [3,2,3]
res = solution.majorityElement(s)
print(res)