
# Exceeding time limits
def threeSum(nums):


    nums.sort()

    sum_list = []
    for i in range(len(nums)):
        n = nums[i]
        need_sum = 0 - n
        l_i = i+1
        r_i = len(nums)-1

        if n > 0:
            break
        if n + nums[r_i-1] + nums[r_i] < 0 or (i > 0 and nums[i] == nums[i-1]):
            continue

        while l_i < r_i:
            if nums[l_i] + nums[r_i] == need_sum:
                if [n, nums[l_i], nums[r_i]] not in sum_list:
                    sum_list.append([n, nums[l_i], nums[r_i]])
                r_i -= 1
                l_i += 1
            elif nums[l_i] + nums[r_i] > need_sum:
                r_i -= 1
            else:
                l_i += 1

    return sum_list


# nums = [-1, 0, 1, 2, -1, -4]
nums = [-1, 0]
# nums = [0,0,0,0]
# nums = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]  # [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]]
# nums = [-3, -4, -2, 0, 2, 2, -2, 1, -1, 2, 3, -1, -5, -4, -5, 1]  # [[-5,2,3],[-4,1,3],[-4,2,2],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-2,1,1],[-1,-1,2],[-1,0,1]]
res = threeSum(nums)
print(res)