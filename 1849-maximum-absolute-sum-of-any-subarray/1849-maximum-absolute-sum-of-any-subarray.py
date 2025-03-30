class Solution:
    def maxAbsoluteSum(self, nums):
        positive, negative, prefixSum, ans = 0, 0, 0, 0
        
        for n in nums:
            prefixSum += n
            ans = max(ans, abs(prefixSum - negative), abs(prefixSum - positive))

            if prefixSum >= 0:
                positive = max(positive, prefixSum)
            else:
                negative = min(negative, prefixSum)

        return ans