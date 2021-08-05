# input = [2, 3, -2, 4]
input = [-2,1,-3,4,-1,2,1,-5,4]
def solution(nums):
    max_opt = 0
    max_memo = [0 for _ in nums]
    min_memo = [0 for _ in nums]
    memo = [0 for _ in nums]
    for i, n in enumerate(nums):
        if i == 0:
            max_memo[0] = n
            min_memo[0] = n
            memo[0] = n
        else:
            max_memo[i] = max(max_memo[i-1] * n, min_memo[i-1] * n, n)
            min_memo[i] = min(max_memo[i-1] * n, min_memo[i-1] * n, n)

        if max_memo[i] > max_opt:
            max_opt = max_memo[i]

    return max_opt


ans = solution(input)
print(ans)
