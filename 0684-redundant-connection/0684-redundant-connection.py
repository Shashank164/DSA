class Solution(object):
    def find(self, dsu, v):
        if dsu[v] != v:
            dsu[v] = self.find(dsu, dsu[v])
        return dsu[v]

    def findRedundantConnection(self, edges):
        dsu = list(range(len(edges) + 1))
        
        for x, y in edges:
            px, py = self.find(dsu, x), self.find(dsu, y)
            if px == py:
                return [x, y]
            dsu[px] = py