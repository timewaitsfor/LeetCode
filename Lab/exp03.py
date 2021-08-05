mat = [
    [1,2,7],
    [2,4,8],
    [3,5,9]
]

num = 4

def solution(mat, num):
    err = 0
    for r_i, row in enumerate(mat):
        for c_i, col_v in enumerate(row):
            if num == col_v:
                err = 1
                return r_i, c_i
    if err == 0:
        return None

num = -1
ans = solution(mat, num)
print(ans)




