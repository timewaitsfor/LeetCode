
# Exceeding time limits
def threeSum(nums):
    nums.sort()

    sum_list = []
    for i in range(1, len(nums)-1):
        n = nums[i]
        need_sum = 0 - n
        l_i = 0
        r_i = len(nums)-1

        if need_sum > nums[-1] + nums[i-1] or need_sum < nums[0] + nums[i+1]:
            continue

        while True:
            if nums[l_i] + nums[r_i] == need_sum:
                if [nums[l_i], n, nums[r_i]] not in sum_list:
                    sum_list.append([nums[l_i], n, nums[r_i]])
                    if r_i-1 > i and l_i+1 < i:
                        r_i -= 1
                        l_i += 1
                    else:
                        break
                else:
                    if r_i-1 > i and l_i+1 < i:
                        r_i -= 1
                        l_i += 1
                    else:
                        break
            elif need_sum > nums[i-1] + nums[r_i] or need_sum < nums[l_i] + nums[i+1]:
                break
            elif nums[l_i] + nums[r_i] > need_sum and r_i-1 > i:
                r_i -= 1
            elif nums[l_i] + nums[r_i] < need_sum and l_i+1 < i:
                l_i += 1
            else:
                break

    return sum_list


# nums = [-1, 0, 1, 2, -1, -4]
# nums = [0,0,0,0]
# nums = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]  # [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]]
nums = [-3, -4, -2, 0, 2, 2, -2, 1, -1, 2, 3, -1, -5, -4, -5, 1]  # [[-5,2,3],[-4,1,3],[-4,2,2],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-2,1,1],[-1,-1,2],[-1,0,1]]
res = threeSum(nums)
print(res)