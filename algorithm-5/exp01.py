
def longestPalindrome(s: str) -> str:

    max_pr_index = None
    max_pr_value = [0]
    for i, c in enumerate(s):

        pr_index = c
        pr_value = [1]

        l_i = i - 1
        r_i = i + 1
        while True:
            l_c = s[l_i] if l_i >= 0 else None
            r_c = s[r_i] if r_i < len(s) else None
            if l_c == pr_index:
                pr_value[len(pr_index)-1] += 1
                l_i = l_i - 1
                continue
            elif r_c == pr_index:
                pr_value[len(pr_index)-1] += 1
                r_i = r_i + 1
                continue
            elif l_c == r_c and l_c != None:
                pr_index = pr_index + l_c
                pr_value.append(1)
                l_i = l_i - 1
                r_i = r_i + 1
            else:
                break

        if (len(pr_value)-1)*2 + pr_value[0] > (len(max_pr_value)-1)*2 + max_pr_value[0]:
            max_pr_index = pr_index
            max_pr_value = pr_value

    pr = max_pr_index[0] * max_pr_value[0]
    for j in range(1, len(max_pr_index)):
        pi = max_pr_index[j]
        pv = max_pr_value[j]
        pr = pi * pv + pr + pi * pv

    return pr


# s = "babad" # bab
# s = "cbbd" # "bb"
# s = "bb" # "bb"
# s = "aaaa" # "aaaa"
s = "aacabdkacaa" # "aca"
res = longestPalindrome(s)
print(res)