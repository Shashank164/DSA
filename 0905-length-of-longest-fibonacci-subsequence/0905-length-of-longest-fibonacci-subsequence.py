class Solution(object):
    def lenLongestFibSubseq(self, arr):
        index_map = {x: i for i, x in enumerate(arr)}
        dp = defaultdict(lambda: 2)
        max_length = 0

        for k in range(len(arr)):
            for j in range(k):
                i = index_map.get(arr[k] - arr[j])
                if i is not None and i < j:
                    dp[j, k] = dp[i, j] + 1
                    max_length = max(max_length, dp[j, k])

        return max_length if max_length >= 3 else 0