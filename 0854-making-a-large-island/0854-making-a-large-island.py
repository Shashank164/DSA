from collections import defaultdict

class Solution:
    def largestIsland(self, grid):
        n = len(grid)
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        island_sizes = defaultdict(int)
        island_id = 2
        max_size = 0

        def dfs(i, j, id):
            if not (0 <= i < n and 0 <= j < n) or grid[i][j] != 1:
                return 0
            grid[i][j] = id
            return 1 + sum(dfs(i + dx, j + dy, id) for dx, dy in dirs)

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    island_sizes[island_id] = dfs(i, j, island_id)
                    max_size = max(max_size, island_sizes[island_id])
                    island_id += 1

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    neighbors = {grid[i + dx][j + dy] for dx, dy in dirs if 0 <= i + dx < n and 0 <= j + dy < n and grid[i + dx][j + dy] > 1}
                    current_size = 1 + sum(island_sizes[id] for id in neighbors)
                    max_size = max(max_size, current_size)

        return max_size if max_size else n * n