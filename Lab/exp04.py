
# 测试range iteration 能否反向
# a = 5
#
# for i in range(a)[::-1]:
#     print(i)

# 测试不用numpy能否进行slice操作
import numpy as np

a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

a = np.array(a)
b = a[:2, :1]

print(b)

