class Solution:
    def coinChange(self, coins, amount: int) -> int:
        dp = [amount+1 for _ in range(amount+1)]
        dp[0] = 0
        for a in range(1, amount+1):
            r = amount+1
            for c in coins:
                need_amount = a - c
                if need_amount < 0:
                    continue
                r = min(r, dp[need_amount]+1)
            dp[a] = r
        if amount == 0:
            return 0
        if r == amount+1:
            return -1
        return r

    def coinChangeToken(self, coins, amount: int) -> int:
        dp = [amount+1 for _ in range(amount+1)]
        dp[0] = 0
        self.coin_types = [0 for _ in range(1, amount+1)]
        for a in range(1, amount+1):
            r = amount+1
            for c in coins:
                need_amount = a - c
                if need_amount < 0:
                    continue
                if r > dp[need_amount]+1:
                    r = dp[need_amount]+1
                    self.coin_types[a-1] = c
                # r = min(r, dp[need_amount]+1)
            dp[a] = r
        if amount == 0:
            return 0
        if r == amount+1:
            return -1
        return r

# ac 1/4
solution = Solution()
# print(solution.coinChange([1],0))
print(solution.coinChangeToken([1,2,5], 11))

this_coin = 11
while True:
    print(solution.coin_types[this_coin-1])
    this_coin = this_coin - solution.coin_types[this_coin-1]
    if this_coin <= 0:
        break

