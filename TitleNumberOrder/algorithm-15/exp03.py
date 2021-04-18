
# Exceeding time limits
def threeSum(nums):
    # nums = list(set(nums))
    # nums.sort()

    sum_list = []
    num_dict = {}
    for i in range(len(nums)):
        n = nums[i]
        if n not in num_dict:
            num_dict[n] = 1
        else:
            num_dict[n] += 1

    for i in range(len(nums)):
        need_sum = 0 - nums[i]
        num_dict[nums[i]] -= 1
        for j in range(i+1, len(nums)):
            if 2*nums[j] == need_sum and num_dict[nums[j]] > 1:
                this_list = [nums[i], nums[j], nums[j]]
                this_list.sort()
                if this_list not in sum_list:
                    sum_list.append(this_list)


            if 2*nums[j] != need_sum and need_sum - nums[j] in num_dict and num_dict[need_sum - nums[j]] > 0:
                this_list = [nums[i], nums[j], need_sum - nums[j]]
                this_list.sort()
                if this_list not in sum_list:
                    sum_list.append(this_list)


    return sum_list


# nums = [-1, 0, 1, 2, -1, -4]
# nums = [0,0,0,0]
# nums = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]  # [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]]
nums = [-3, -4, -2, 0, 2, 2, -2, 1, -1, 2, 3, -1, -5, -4, -5, 1]  # [[-5,2,3],[-4,1,3],[-4,2,2],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-2,1,1],[-1,-1,2],[-1,0,1]]
res = threeSum(nums)
print(res)