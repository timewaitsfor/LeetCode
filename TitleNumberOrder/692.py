class Solution:
    def topKFrequent(self, words, k: int):
        memo = {}
        for word in words:
            if word not in memo:
                memo[word] = 1
            else:
                memo[word] += 1

        count_dict = {}

        for word_n, word_c in memo.items():
            if word_c not in count_dict:
                count_dict[word_c] = [word_n]
            else:
                for idx, common_word in enumerate(count_dict[word_c]):
                    if common_word < word_n:
                        continue
                    else:
                        count_dict[word_c].insert(idx, word_n)
                        break
                if idx < len(count_dict[word_c])-1:
                    count_dict[word_c].append(word_n)

        ranked_count = list(count_dict.keys())
        ranked_count.sort(reverse=True)

        res = []
        for rc in ranked_count:
            r_w = count_dict[rc]
            res += r_w
            if len(res) >= k:
                return res[:k]

solution = Solution()
# words = ["i", "love", "leetcode", "i", "love", "coding"]
words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
# k = 2
res = solution.topKFrequent(words, k)
print(res)