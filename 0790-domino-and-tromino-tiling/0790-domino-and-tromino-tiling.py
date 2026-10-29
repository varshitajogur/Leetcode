class Solution:
    def numTilings(self, n):
        MOD = 10**9 + 7

        if n == 1:
            return 1
        if n == 2:
            return 2

        a = 1
        b = 1
        c = 2

        for i in range(3, n + 1):
            d = (2 * c + a) % MOD

            a = b
            b = c
            c = d

        return c