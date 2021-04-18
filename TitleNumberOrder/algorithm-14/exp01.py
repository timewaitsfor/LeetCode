
def longestCommonPrefix(strs) -> str:
    if len(strs) == 0:
        return ""
    cp = strs[0]
    for i in range(len(strs)):
        head_strs = cp
        tail_strs = strs[i]

        this_cp = ""
        for j in range(min(len(head_strs), len(tail_strs))):
            if head_strs[j] == tail_strs[j]:
                this_cp += head_strs[j]
            else:
                break
        cp = this_cp
        if cp == "":
            break
    return cp


# strs = ["flower","flow","flight"]
strs = ["dog","racecar","car"]
res = longestCommonPrefix(strs)

print(res)