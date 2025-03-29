class Solution:
    def eventualSafeNodes(self, graph):
        def dfs(node):
            if state[node] != 0:
                return state[node] == 2
            state[node] = 1
            if any(state[neighbor] == 1 or not dfs(neighbor) for neighbor in graph[node]):
                return False
            state[node] = 2
            return True

        state = [0] * len(graph)
        return [i for i in range(len(graph)) if dfs(i)]
        