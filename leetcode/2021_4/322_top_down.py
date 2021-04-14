class Solution:
    def __init__(self):
        self.valid_ret = 1000000
    def coinChange(self, coins, amount) :
        self.coins = sorted(coins,reverse=True)
        self.len = len(self.coins)
        self.amount = amount
        self.cache = [0 for i in range(self.amount+1 )]
        # for c in self.coins:
        #     self.cache[c] = 1
        ret= self.dp(amount)
        if ret >= self.valid_ret:
            return -1
        else:
            return ret

    def dp(self, val):
        if val < 1:
            return self.valid_ret
        if val <= self.coins[0] and val in self.coins:
            return 1
        min_ret = self.valid_ret
        for c in self.coins:
            ret = self.dp(val-c) + 1
            if ret < min_ret:
                return ret
        return min_ret