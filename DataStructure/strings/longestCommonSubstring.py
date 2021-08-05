s1 = "abcde"
s2 = "hbcdef"

def common_str(s1, s2):
    m, n = len(s1), len(s2)
    dp  = [[0 for _ in range(n+1)] for _ in range(m+1)]
    max_common_str_len = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = 0

            if dp[i][j] > max_common_str_len:
                max_common_str_len = dp[i][j]
    return max_common_str_len

ans = common_str(s1, s2)
print(ans)