class Solution(object):
    def countBadPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        map=defaultdict(int)
        cntBadPair=(n-1)*n/2
        for i in range(0, n):
            val=map[nums[i]-i]
            cntBadPair-=val
            map[nums[i]-i]=val+1

        return cntBadPair