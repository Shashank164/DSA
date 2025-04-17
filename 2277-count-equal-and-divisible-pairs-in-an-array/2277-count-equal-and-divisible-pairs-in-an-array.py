class Solution(object):
    def countPairs(self, nums, k):
        c=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j] and (i*j)%k==0:
                    c=c+1
        return c
        