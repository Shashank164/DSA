class Solution(object):
    def countBadPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=0
        mp={}
        for i in range(len(nums)):
            dif=nums[i]-i
            if dif in mp:
                res+=mp[dif]
            mp[dif]=mp.get(dif,0)+1
        total=len(nums)*(len(nums)-1)//2
        return total-res