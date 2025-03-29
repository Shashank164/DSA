class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = map(sum, grid), map(sum, zip(*grid))
        return sum(grid[i][j] and (rows[i] > 1 or cols[j] > 1) 
            for i in range(len(grid)) for j in range(len(grid[0]))) 