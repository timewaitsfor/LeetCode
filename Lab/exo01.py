# strs = [["10", "0001", "111001", "1", "0"],[1]]

# print(int('0' == '0'))
# print(int('1' == '0'))

# [print(_) for _ in range(1, 2)]

# print(3&2)

# print([_ for _ in range(3)][:4])

a = [_ for _ in range(3)]
b = a[::-1]

if a == b[::-1]:
    print(True)

# print(str(strs))
# print(hash(strs))
# print(strs[0][1])
# i = 2
#
# print(strs[:i]+strs[i+1:])


# def get_str_info(ss):
#     m, n = 0, 0
#     for s in ss:
#         for c in s:
#             if c == "0":
#                 m += 1
#             else:
#                 n += 1
#     return m, n
#
# def find_max_subset(strs, m, n):
#     _m, _n = get_str_info(strs)
#     if _m <= m and _n <= n:
#         return strs
#
#     max_subset_c = -1
#     max_subset = []
#     for i, s in enumerate(strs):
#         this_m, this_n = get_str_info(s)
#         need_m, need_n = m - this_m, n - this_n
#         if need_m < 0 or need_n < 0:
#             continue
#         need_subset = find_max_subset(strs[:i] + strs[i + 1:], need_m, need_n)
#         if len(need_subset) + 1 > max_subset_c:
#             max_subset_c = len(need_subset) + 1
#             max_subset = [s] + need_subset
#
#     if max_subset_c == -1:
#         return []
#
#     return max_subset


# print(get_str_info(["10", "0001", "111001", "1", "0"]))
# print(find_max_subset(strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3))