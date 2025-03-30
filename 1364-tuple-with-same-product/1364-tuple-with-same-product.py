from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums):
        product_count = defaultdict(int)
        result = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                result += product_count[product]
                product_count[product] += 1

        return result * 8