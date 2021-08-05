
class Solution:
    def isValid(self, s: str) -> bool:
        memo = []
        brackets_dict = {}
        brackets_dict['('] = ')'
        brackets_dict['['] = ']'
        brackets_dict['{'] = '}'
        if s == '':
            return False

        length = len(s)
        for i in range(length):
            if len(memo) == 0:
                memo.append(s[i])
                continue
            source_t = memo[-1]
            target_t = s[i]
            if source_t not in brackets_dict:
                return False
            anchor_t = brackets_dict[source_t]
            if target_t == anchor_t:
                memo.pop(-1)
            else:
                memo.append(target_t)

        if len(memo) == 0:
            return True
        else:
            return False

s = "()[]{}"
solution = Solution()
ans = solution.isValid(s)
print(ans)