class Solution:
    def shortestCommonSupersequence(self, A, B):
        def lcs(A, B):
            n, m = len(A), len(B)
            dp = [["" for _ in range(m + 1)] for _ in range(n + 1)]
            for i in range(n):
                for j in range(m):
                    if A[i] == B[j]:
                        dp[i + 1][j + 1] = dp[i][j] + A[i]
                    else:
                        dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1], key=len)
            return dp[-1][-1]

        lcs_str = lcs(A, B)
        i = j = 0
        res = []
        for c in lcs_str:
            while A[i] != c:
                res.append(A[i])
                i += 1
            while B[j] != c:
                res.append(B[j])
                j += 1
            res.append(c)
            i += 1
            j += 1
        return "".join(res) + A[i:] + B[j:]