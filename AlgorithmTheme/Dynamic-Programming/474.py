class BroteForceSolution:
    # 给一个字符串返回它0和1的个数
    def get_str_info(self, ss):
        m, n = 0, 0
        for s in ss:
            for c in s:
                if c == '0':
                    m += 1
                else:
                    n += 1
        return m, n

    def find_max_subset(self, strs, m, n):
        _m, _n = self.get_str_info(strs)
        if _m <= m and _n <= n:
            return strs

        max_subset_c = -1
        max_subset = []
        for i, s in enumerate(strs):
            this_m, this_n = self.get_str_info(s)
            need_m, need_n = m - this_m, n - this_n
            if need_m < 0 or need_n < 0:
                continue
            need_subset = self.find_max_subset(strs[:i] + strs[i + 1:], need_m, need_n)
            if len(need_subset) + 1 > max_subset_c:
                max_subset_c = len(need_subset) + 1
                max_subset = [s] + need_subset

        if max_subset_c == -1:
            return []

        return max_subset

    def findMaxForm(self, strs, m: int, n: int) -> int:

        opt_subset = self.find_max_subset(strs, m, n)

        print(strs, m, n)
        print(opt_subset)
        return len(opt_subset)

class FakeDPSolution:

    def dp_init(self, max_r, max_c):
        self.dp_table = {}

        self.str_info_table = {}

        self.max_r_l = range(max_r+1)
        self.max_c_l = range(max_c+1)

    def dp_table_matrix_init(self, subset, dp_table_matrix, m, n):

        if dp_table_matrix == []:
            for i in self.max_r_l:
                dp_table_matrix.append([])
                for j in self.max_c_l:
                    dp_table_matrix[i].append(None)
                    if i == m and j == n:
                        dp_table_matrix[i][j] = subset
        else:
            dp_table_matrix[m][n] = subset

        return dp_table_matrix

    # 给一个字符串返回它0和1的个数
    def get_str_info(self, ss):
        m, n = 0, 0
        for s in ss:
            for c in s:
                if c == '0':
                    m += 1
                else:
                    n += 1
        return m, n

    def find_max_subset(self, strs, m, n):

        if str(strs) not in self.str_info_table:
            _m, _n = self.get_str_info(strs)
            self.str_info_table[str(strs)] = [_m, _n]
        else:
            [_m, _n] = self.str_info_table[str(strs)]


        if _m <= m and _n <= n:
            return strs

        max_subset_c = -1
        max_subset = []
        for i, s in enumerate(strs):
            if str(s) not in self.str_info_table:
                this_m, this_n = self.get_str_info(s)
                self.str_info_table[str(s)] = [this_m, this_n]
            else:
                [this_m, this_n] = self.str_info_table[str(s)]

            need_m, need_n = m - this_m, n - this_n
            if need_m < 0 or need_n < 0:
                continue

            cut_subset = strs[:i] + strs[i + 1:]
            if str(cut_subset) not in self.dp_table:
                need_subset = self.find_max_subset(cut_subset, need_m, need_n)
                self.dp_table[str(cut_subset)] = self.dp_table_matrix_init(need_subset, [],need_m, need_n)
            else:
                if self.dp_table[str(cut_subset)][need_m][need_n] != None:
                    need_subset = self.dp_table[str(cut_subset)][need_m][need_n]
                else:
                    need_subset = self.find_max_subset(cut_subset, need_m, need_n)
                    self.dp_table[str(cut_subset)] = self.dp_table_matrix_init(need_subset, self.dp_table[cut_subset], need_m, need_n)


            if len(need_subset) + 1 > max_subset_c:
                max_subset_c = len(need_subset) + 1
                max_subset = [s] + need_subset

        if max_subset_c == -1:
            return []

        return max_subset

    def findMaxForm(self, strs, m: int, n: int) -> int:

        self.dp_init(m, n)
        opt_subset = self.find_max_subset(strs, m, n)

        # print(self.dp_table, 111)
        return len(opt_subset)

class Solution:
    def count_zeros_ones(self, s):
        m_n = [0, 0]
        for c in s:
            m_n[int(c=='1')] += 1
        return m_n

    def findMaxForm(self, strs, m: int, n: int) -> int:
        dp = [[[0 for __ in range(n+1)] for _ in range(m+1)] for k in range(len(strs))]
        for k, s in enumerate(strs):
            this_m_n = self.count_zeros_ones(s)
            for i in range(m+1):
                for j in range(n+1):
                    need_m, need_n = i - this_m_n[0], j - this_m_n[1]
                    if need_m < 0 or need_n < 0:
                        dp[k][i][j] = dp[k-1][i][j]
                    else:
                        if k == 0:
                            dp[k][i][j] = 1
                        else:
                            dp[k][i][j] = max(dp[k-1][i][j], dp[k-1][need_m][need_n]+1)
        return dp[len(strs)-1][m][n]

    # 2021-04-23 10:59:03 二刷 【failed】
    def findMaxForm01(self, strs, m: int, n: int):
        memo = [[0 for _ in range(n+1)] for __ in range(m+1)]
        for s in strs:
            this_m_n = self.count_zeros_ones(s)
            if this_m_n[0] > m or this_m_n[1] > n:
                continue

            for i in range(this_m_n[0], m+1)[::-1]:
                for j in range(this_m_n[1], n+1)[::-1]:
                    memo[i][j] = max(memo[i][j], memo[i-this_m_n[0]][j-this_m_n[1]]+1)
        return memo[m][n]




# ['10', '0001', '1', '0']
# solution = BroteForceSolution()
solution = Solution()

# strs = ["10", "0", "1"]
# m = 1
# n = 1

strs = ["10","0001","111001","1","0"]
m = 5
n = 3

# opt = solution.findMaxForm(strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3)
# opt = solution.findMaxForm(strs, m, n)
opt = solution.findMaxForm01(strs, m, n)
print(opt)
