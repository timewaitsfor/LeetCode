
class rod_cutting_solution:

    def brute_force_algorithem(self, p, n):
        if n <= 0:
            return 0
        r = 0
        for idx, i in enumerate(range(1, len(p)+1)):
            this_r = p[idx]
            if n < i:
                continue
            r = max(r, this_r+self.brute_force_algorithem(p, n-i))
        return r

    def dynamic_pro_init(self, n):
        self.memo = [-1 for _ in range(n)]

    def dynamic_pro_algorithm(self, p, n):
        if n <= 0:
            return 0
        if self.memo[n-1] != -1:
            r = self.memo[n]
        else:
            r = 0
            for idx, i in enumerate(range(1, len(p)+1)):
                this_r = p[idx]
                if n < i:
                    continue
                r = max(r, this_r+self.dynamic_pro_algorithm(p, n-i))
        return r

    def bottom_up_dp(self, p, n):
        for i in range(1, n+1):
            r = 0
            for j, v in enumerate(p):
                l = j+1
                if i-l <= 0:
                    continue
                r = max(r, v+self.memo[i-l-1])
            self.memo[i-1] = r
        return r




# input
p = [1, 5, 8, 9, 10]
n = 4

# output
r = 10

# solution
solution = rod_cutting_solution()
# brute_force_solution = solution.brute_force_algorithem(p, n)
# print(brute_force_solution)

solution.dynamic_pro_init(n)
# dynamic_pro_solution = solution.dynamic_pro_algorithm(p, n)
# print(dynamic_pro_solution)

bu_dp_solution = solution.dynamic_pro_algorithm(p, n)

print(bu_dp_solution)