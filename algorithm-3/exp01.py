
def lengthOfLongestSubstring(s: str) -> int:

    source_s = ""
    max_s = ""

    for i, c in enumerate(s):
        if source_s == "":
            source_s = c
            max_s = source_s
            continue

        tem_k = -1
        for j, s_c in enumerate(source_s):
            if c == s_c:
                tem_k = j
                break

        if tem_k == -1:
            source_s = source_s + c
        elif tem_k+1 == len(source_s):
            source_s = c
        else:
            source_s = source_s[tem_k+1:]+c

        if len(source_s) > len(max_s):
            max_s = source_s

    return len(max_s)

# s = "abcabcbb" # 3
# s = "bbbbb" # 1
s = "pwwkew" # 3
res = lengthOfLongestSubstring(s)
print(res)
