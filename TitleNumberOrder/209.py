class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:

        if sum(nums) < target:
            return 0
        res = len(nums)
        queue = []

        this_sum = 0
        for n in nums:
            if this_sum >= target:
                while len(queue) != 0 and this_sum >= target:
                    if len(queue) < res:
                        res = len(queue)
                    this_sum -= queue[0]
                    queue.pop(0)
            queue.append(n)
            this_sum += n

        if this_sum >= target:
            while len(queue) != 0 and this_sum >= target:
                if len(queue) < res:
                    res = len(queue)
                this_sum -= queue[0]
                queue.pop(0)
        return res


solution = Solution()
k = 7
nums = [2,3,1,2,4,3]
res = solution.minSubArrayLen(k, nums)
print(res)