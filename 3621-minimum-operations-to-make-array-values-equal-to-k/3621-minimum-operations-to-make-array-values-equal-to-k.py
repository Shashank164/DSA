class Solution(object):
    def minOperations(self, nums, k):
        mpp = {}
        for i in nums:
            if i < k:
                return -1
            elif i > k:
                mpp[i] = mpp.get(i, 0) + 1
        return len(mpp)