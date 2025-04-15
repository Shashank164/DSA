class Solution(object):
    def goodTriplets(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n = len(nums1)
        
        # Map each value to its index in nums2
        pos_in_nums2 = [0] * n
        for i in range(n):
            pos_in_nums2[nums2[i]] = i
        
        # Create the mapped version of nums1 based on positions in nums2
        mapped = [pos_in_nums2[val] for val in nums1]
        
        # Fenwick Tree helpers
        class FenwickTree:
            def __init__(self, size):
                self.tree = [0] * (size + 1)

            def update(self, index, value):
                index += 1
                while index < len(self.tree):
                    self.tree[index] += value
                    index += index & -index

            def query(self, index):
                # Sum from 0 to index
                index += 1
                result = 0
                while index > 0:
                    result += self.tree[index]
                    index -= index & -index
                return result

        # Count leftLess[i]: how many values before i are smaller
        left_tree = FenwickTree(n)
        left_less = [0] * n
        for i in range(n):
            left_less[i] = left_tree.query(mapped[i] - 1)
            left_tree.update(mapped[i], 1)

        # Count rightGreater[i]: how many values after i are greater
        right_tree = FenwickTree(n)
        right_greater = [0] * n
        for i in reversed(range(n)):
            right_greater[i] = right_tree.query(n - 1) - right_tree.query(mapped[i])
            right_tree.update(mapped[i], 1)

        # Total number of good triplets
        result = 0
        for i in range(n):
            result += left_less[i] * right_greater[i]

        return result