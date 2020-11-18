


class Solution:
    def isValid(self, s: str) -> bool:

        bracket_dict = {}
        bracket_dict[')'] = '('
        bracket_dict['}'] = '{'
        bracket_dict[']'] = '['

        stack = []
        for i, bracket in enumerate(s):
            if stack == [] or bracket not in bracket_dict:
                stack.append(bracket)
            else:
                if bracket_dict[bracket] != stack[-1]:
                    stack.append(bracket)
                else:
                    stack.pop()

        return stack == []


solu = Solution()
# s = "()"
# s = "{[]}"
s = "(]"
res = solu.isValid(s)
print(res)