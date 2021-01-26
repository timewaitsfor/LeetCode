

def isPalindrome(x: int) -> bool:

    if x < 0 or (x!=0 and x%10 == 0):
        return False
    else:
        n_x = 0
        while True:
            n_x = n_x * 10 + x % 10
            if int(x / 10) > n_x:
                x = int(x / 10)
            elif int(x / 10) == n_x:
                x = int(x / 10)
                break
            else:
                break

        if n_x == x:
            return True
        else:
            return False

# print(121%1000)

# x = -121 # false
# x = 110 # false
x = 1230 # false
# x = 1221 # true
# x = 121 # true
res = isPalindrome(x)
print(res)