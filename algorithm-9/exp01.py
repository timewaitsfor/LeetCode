
def isPalindrome(x: int) -> bool:
    x = str(x)
    res = True
    for i, n in enumerate(x):
        p_n = n
        n_n = x[-i-1]
        if p_n != n_n:
            res = False
    return res

# x = -121 # false
# x = 10 # false
x = 121 # true
res = isPalindrome(x)
print(res)