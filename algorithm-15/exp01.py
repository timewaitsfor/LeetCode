
# error version
def threeSum(nums):

    # nums = list(set(nums))
    nums.sort()

    sum_list = []
    for i in range(1, len(nums)-1):
        n = nums[i]
        need_sum = 0 - n
        l_i = i-1
        r_i = i+1

        if n == 0:
            print()

        while True:
            if nums[l_i] + nums[r_i] == need_sum and [nums[l_i], n, nums[r_i]] not in sum_list:
                sum_list.append([nums[l_i], n, nums[r_i]])
                if r_i+1 < len(nums) and l_i-1 >= 0:
                    r_i += 1
                    l_i -= 1
                else:
                    break

            elif nums[l_i] + nums[r_i] < need_sum and r_i+1 < len(nums):
                r_i += 1
            elif nums[l_i] + nums[r_i] > need_sum and l_i-1 >= 0:
                l_i -= 1
            else:
                break

    return sum_list


# nums = [-1, 0, 1, 2, -1, -4]
# nums = [0,0,0,0]
nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6] # [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]]
res = threeSum(nums)

print(res)