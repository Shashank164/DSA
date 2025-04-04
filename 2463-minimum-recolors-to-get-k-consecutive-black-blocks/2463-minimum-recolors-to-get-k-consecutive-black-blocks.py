class Solution(object):
    def minimumRecolors(self, blocks, k):
        n = len(blocks)
        min_operations = float('inf')
        
        # Initial count of 'W' in the first window
        white_count = blocks[:k].count('W')
        min_operations = white_count
        
        # Slide the window across the string
        for i in range(1, n - k + 1):
            if blocks[i - 1] == 'W':
                white_count -= 1
            if blocks[i + k - 1] == 'W':
                white_count += 1
            min_operations = min(min_operations, white_count)
        
        return min_operations