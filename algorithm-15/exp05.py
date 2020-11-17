
# I want to move the left and right pointers of the array and then use a for-in statement to determine if any
# (0 - l_num - r_num )number exist.

# Exceeding time limits
def get_need_num(l_i, r_i, nums, sum_list):
    l_n = nums[l_i]
    r_n = nums[r_i]
    need_n = -l_n - r_n

    if need_n < l_n or need_n > r_n:
        return sum_list

    else:
        if [l_n, need_n, r_n] not in sum_list:
            sum_list.append([l_n, need_n, r_n])

        this_l_i = l_i
        this_r_i = r_i
        if this_l_i+1 < r_i:
            this_l_i += 1
            while nums[this_l_i] == l_n:
                this_l_i += 1
            sum_list += get_need_num(this_l_i, r_i, nums, sum_list)

        if this_r_i-1 > l_i:
            this_r_i -= 1
            while nums[this_r_i] == r_n:
                this_r_i -= 1
            sum_list += get_need_num(l_i, this_r_i, nums, sum_list)

        return sum_list

def threeSum(nums):
    sum_list = []
    nums.sort()
    l_i = 0
    r_i = len(nums) - 1
    sum_list = get_need_num(l_i, r_i, nums, sum_list)

    return sum_list


nums = [-1, 0, 1, 2, -1, -4]
# nums = [0,0,0,0]
# nums = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]  # [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]]
# nums = [-3, -4, -2, 0, 2, 2, -2, 1, -1, 2, 3, -1, -5, -4, -5, 1]  # [[-5,2,3],[-4,1,3],[-4,2,2],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-2,1,1],[-1,-1,2],[-1,0,1]]
res = threeSum(nums)
print(res)