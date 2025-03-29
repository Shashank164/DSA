class Solution(object):
    def magnificentSets(self, n, edges):
        graph = [[] for _ in range(n)]

        for start, end in edges:
            graph[start - 1].append(end - 1)
            graph[end - 1].append(start - 1)

        distances = [0] * n

        for i in range(n):
            queue = deque([i])
            distance_map = [0] * n
            distance_map[i] = 1
            max_dist = 1
            root_node = i

            while queue:
                current_node = queue.popleft()
                root_node = min(root_node, current_node)

                for neighbor in graph[current_node]:
                    if distance_map[neighbor] == 0:
                        distance_map[neighbor] = distance_map[current_node] + 1
                        max_dist = max(max_dist, distance_map[neighbor])
                        queue.append(neighbor)
                    elif abs(distance_map[neighbor] - distance_map[current_node]) != 1:
                        return -1

            distances[root_node] = max(distances[root_node], max_dist)

        return sum(distances)

