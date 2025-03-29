from collections import deque

class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        adj = [[] for _ in range(numCourses)]
        prereq = [0] * numCourses
        in_degree = [0] * numCourses

        for a, b in prerequisites:
            adj[a].append(b)
            prereq[b] |= 1 << a
            in_degree[b] += 1

        q = deque([i for i in range(numCourses) if in_degree[i] == 0])

        while q:
            u = q.popleft()
            for v in adj[u]:
                prereq[v] |= prereq[u]
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)

        return [(prereq[v] & (1 << u)) != 0 for u, v in queries]