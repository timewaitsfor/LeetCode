class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        memo = {}
        for c in t:
            if c not in memo:
                memo[c] = 1
            else:
                memo[c] += 1

        for cc in s:
            memo[cc] -= 1

        res = ""
        for ccc in memo:
            if memo[ccc] >= 1:
                res += ccc

        return res


s = "ae"
t = "aea"

solution = Solution()
res = solution.findTheDifference(s, t)