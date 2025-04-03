class Solution(object):
    def longestMonotonicSubarray(self, nums):
        n=len(nums)

        inc = dec= res = 1
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                dec+=1
                inc=1
            elif nums[i]<nums[i+1]:
                inc+=1
                dec=1
            else:
                inc = dec = 1

            res=max(inc,dec,res)
        return res
