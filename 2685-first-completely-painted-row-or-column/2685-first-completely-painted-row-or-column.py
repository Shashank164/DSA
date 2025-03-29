class Solution(object):
    def firstCompleteIndex(self, arr, mat):
        """
        :type arr: List[int]
        :type mat: List[List[int]]
        :rtype: int
        """
        m, n = len(mat), len(mat[0])

        # Initialize frequency counters for rows and columns
        row_freq = [0] * m
        col_freq = [0] * n

        # Create a dictionary to map matrix values to their coordinates
        value_to_index = {mat[i][j]: (i, j) for i in range(m) for j in range(n)}

        # Traverse through arr and update row and column frequencies
        for i, value in enumerate(arr):
            r, c = value_to_index[value]
            row_freq[r] += 1
            col_freq[c] += 1

            # Check if any row or column is completely filled
            if row_freq[r] == n or col_freq[c] == m:
                return i

        return -1

        