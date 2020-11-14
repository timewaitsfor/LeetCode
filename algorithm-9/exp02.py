

def isPalindrome(x: int) -> bool:

    t_x = x
    if x < 0:
        return False
    else:
        i = 1
        n_x = 0
        while True:
            mod = 10**i
            tens = 10**(i-1)
            n_x = (t_x % mod)/tens + n_x*10
            t_x -= t_x % mod
            i += 1
            if x % mod == x:
                break

        if n_x == x:
            return True
        else:
            return False

# print(121%1000)

# x = -121 # false
x = 10 # false
# x = 121 # true
res = isPalindrome(x)
print(res)