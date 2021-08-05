

str1 = "abcdacd"
pat1 = "acd"

def str_search(pat, txt):
    m = len(pat)
    n = len(txt)
    i = 0
    j = 0
    while True:
        if  i >= n or j >= m:
            break
        if txt[i] == pat[j]:
            j += 1
        else:
            i -= j
            j = 0
        i += 1

    if j == m:
        return i - m
    else:
        return n

ans = str_search(pat1, str1)
print(ans)