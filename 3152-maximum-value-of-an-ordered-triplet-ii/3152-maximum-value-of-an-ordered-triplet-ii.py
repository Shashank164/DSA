class Solution(object):
    def maximumTripletValue(self, nums):
        max_triplet = 0
        max_element = 0
        max_diff = 0

        for num in nums:
            max_triplet = max(max_triplet, max_diff * num)
            max_diff = max(max_diff, max_element - num)
            max_element = max(max_element, num)

        return max_triplet