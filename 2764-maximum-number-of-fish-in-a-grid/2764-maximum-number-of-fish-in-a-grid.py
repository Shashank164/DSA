from collections import deque

class Solution:
    def findMaxFish(self, grid):
        m, n = len(grid), len(grid[0])
        ans = 0
        vis = [[False] * n for _ in range(m)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(i, j):
            q = deque([(i, j)])
            vis[i][j] = True
            current_fish = 0
            while q:
                row, col = q.popleft()
                current_fish += grid[row][col]
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < m and 0 <= nc < n and not vis[nr][nc] and grid[nr][nc] > 0:
                        vis[nr][nc] = True
                        q.append((nr, nc))
            return current_fish

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and not vis[i][j]:
                    ans = max(ans, bfs(i, j))

        return ans