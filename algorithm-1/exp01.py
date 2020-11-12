
def twoSum(nums, target):
    two_sum_duplicate_dict = {}
    two_sum_dict = {}

    for i, n in enumerate(nums):
        if n in two_sum_dict:
            if n in two_sum_duplicate_dict:
                continue
            two_sum_duplicate_dict[n] = i
        else:
            two_sum_dict[n] = i

    for i, n in enumerate(nums):
        sub_n = target - n
        if sub_n == target/2 and sub_n in two_sum_duplicate_dict:
            return two_sum_dict[n], two_sum_duplicate_dict[n]
        elif sub_n == target/2:
            continue

        if sub_n in two_sum_dict:
            source_i = two_sum_dict[n]
            target_i = two_sum_dict[sub_n]
            if source_i > target_i:
                return target_i, source_i
            else:
                return source_i, target_i



# nums = [2, 7, 11, 15]
nums = [3,2,4]
# target = 9
target = 6

res = twoSum(nums, target)
print(res)

