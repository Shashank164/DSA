class Solution(object):
    def gridGame(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid[0])
        top_sum, bottom_sum = sum(grid[0]), 0
        res = float('inf')
        
        for i in range(m):
            top_sum -= grid[0][i]
            res = min(res, max(top_sum, bottom_sum))
            bottom_sum += grid[1][i]
        
        return res
