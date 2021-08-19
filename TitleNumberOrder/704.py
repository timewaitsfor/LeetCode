
def search(nums, target: int) -> int:
    left_idx = 0
    right_idx = len(nums ) -1

    while left_idx < right_idx:
        mid_idx = int((right_idx - left_idx ) /2) + left_idx
        if target < nums[mid_idx]:
            right_idx = mid_idx-1
        elif target > nums[mid_idx]:
            left_idx = mid_idx+1
        else:
            return mid_idx

    if nums[left_idx] == target:
        return left_idx
    else:
        return -1


res = search([-1,0,3,5,9,12], 2)
print(res)