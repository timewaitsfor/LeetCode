class Solution:
    # 错误解法，对s = "aaaaaaa"，wordDict = ["aaaa","aaa"]无效
    def wordBreak01(self, s, wordDict) -> bool:
        l = 0
        r = 1
        while True:
            if r == len(s):
                break
            this_s = s[l:r]
            if this_s in wordDict:
                l = r
            r += 1
        if s[l:r] not in wordDict:
            return False
        else:
            return True

    def wordBreak02(self, s, wordDict) -> bool:
        l = len(s)
        dp = [0 for _ in range(l+1)]
        dp[0] = 1
        for i in range(1, l+1):
            for j in range(0, i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = 1
                    break
        return bool(dp[-1])


# s = "leetcodes"
# s = "applepenapple"
# s = "catsandog"
s = "aaaaaaa"
# wordDict = ["leet", "code"]
# wordDict = ["apple", "pen"]
# wordDict = ["cats", "dog", "sand", "and", "cat"]
wordDict = ["aaaa","aaa"]


solution = Solution()
ans = solution.wordBreak02(s, wordDict)
print(ans)