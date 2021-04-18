

def solution(n, lists):
    memo = []
    max_len = len(lists)
    left = 0
    right = 0

    while True:
        val = lists[right]
        max_len = min(max_len, val)
        if len(memo) == 0:
            memo.append(val)
        if max_len < len(memo):
            left = right - max_len
            right += 1
        else:
            right += 1







    pass


res = solution(5, [1,3,4,5,2])
print(res)