class Solution:
    def numOfSubarrays(self, arr):
        mod = 10**9 + 7
        dp = [[0] * (len(arr) + 1) for _ in range(2)]
        res = 0

        for i in range(len(arr) - 1, -1, -1):
            if arr[i] % 2 == 1:  # Odd number
                dp[1][i] = (dp[0][i + 1] + 1) % mod
                dp[0][i] = dp[1][i + 1] % mod
            else:  # Even number
                dp[1][i] = dp[1][i + 1] % mod
                dp[0][i] = (dp[0][i + 1] + 1) % mod
            
            res = (res + dp[1][i]) % mod
        
        return res