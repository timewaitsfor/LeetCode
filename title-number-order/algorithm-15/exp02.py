
# Exceeding time limits
def threeSum(nums):
    # nums = list(set(nums))
    nums.sort()

    sum_list = []
    for i in range(1, len(nums) - 1):
        n = nums[i]
        need_sum = 0 - n

        l_dict = {}
        r_dict = {}
        for l_i in range(0, i):
            l_dict[nums[l_i]] = l_i

        for r_i in range(i+1, len(nums)):
            r_dict[nums[r_i]] = r_i

        for j in range(0, i):
            need_num = need_sum - nums[j]
            if need_num in r_dict and [nums[j], n, need_num] not in sum_list:
                sum_list.append([nums[j], n, need_num])

    return sum_list


# nums = [-1, 0, 1, 2, -1, -4]
# nums = [0,0,0,0]
nums = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]  # [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]]
res = threeSum(nums)

print(res)