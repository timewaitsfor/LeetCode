class Solution:
    def reverseAndReturn(self, s):
        if len(s) == 1:
            return s
        thisChar = s.pop(0)
        this_reverse = self.reverseAndReturn(s)
        this_reverse.append(thisChar)
        return this_reverse


    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        return self.reverseAndReturn(s)

solution = Solution()

s = ["h","e","l","l","o"]
res = solution.reverseString(s)
print(res)