import heapq

class Solution:
    def trapRainWater(self, heightMap):
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        minHeap = []

        # Add boundary cells to the heap and mark them as visited
        for i in range(m):
            for j in (0, n - 1):
                heapq.heappush(minHeap, (heightMap[i][j], i, j))
                visited[i][j] = True
        for j in range(n):
            for i in (0, m - 1):
                if not visited[i][j]:
                    heapq.heappush(minHeap, (heightMap[i][j], i, j))
                    visited[i][j] = True

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        waterTrapped = 0

        while minHeap:
            height, x, y = heapq.heappop(minHeap)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    waterTrapped += max(0, height - heightMap[nx][ny])
                    heapq.heappush(minHeap, (max(height, heightMap[nx][ny]), nx, ny))
                    visited[nx][ny] = True

        return waterTrapped