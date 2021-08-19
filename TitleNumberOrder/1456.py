class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        i = 0
        j = 0
        total = 0
        vow = ['a', 'e', 'i', 'o', 'u']

        length = len(s)
        while i < length:
            if s[i] in vow:
                total += 1
                break
            i += 1

        if i == length:
            return total

        for j in range(i + 1, min(i + k, length)):
            if s[j] in vow:
                total += 1

        res = total

        while j < length - 1:
            if total > res:
                res = total

            if s[i] in vow:
                total -= 1
            i += 1
            j += 1
            if s[j] in vow:
                total += 1

        return max(res, total)


solution = Solution()

s = "weallloveyou"
k = 7
res = solution.maxVowels(s, k)
print(res)