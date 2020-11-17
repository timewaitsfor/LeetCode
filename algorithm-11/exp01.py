def maxArea(height) -> int:

    max_area = 0
    l_i = 0
    r_i = len(height) - 1

    while True:
        this_area = min(height[l_i], height[r_i])*(r_i - l_i)
        if this_area > max_area:
            max_area = this_area

        if height[l_i] >= height[r_i]:
            r_i -= 1
        else:
            l_i += 1

        if l_i >= r_i:
            break

    return max_area



# height = [1,8,6,2,5,4,8,3,7] # 49
# height = [1, 1] # 1
# height = [4,3,2,1,4] # 16
height = [1,2,1] # 2

res = maxArea(height)
print(res)