class Solution(object):
    def numTilePossibilities(self, tiles):
        def dfs(counter):
            total = 0
            for char in counter:
                if counter[char] > 0:
                    total += 1
                    counter[char] -= 1
                    total += dfs(counter)
                    counter[char] += 1
            return total

        return dfs(Counter(tiles))