class Solution(object):
    def punishmentNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        def can_partition(num_str, target):
            def backtrack(start, current_sum):
                if current_sum > target:
                    return False
                if start == len(num_str):
                    return current_sum == target
                return any(backtrack(end, current_sum + int(num_str[start:end])) 
                for end in range(start + 1, len(num_str) + 1))
            
            return backtrack(0, 0)

        return sum(i * i for i in range(1, n + 1) if can_partition(str(i * i), i))