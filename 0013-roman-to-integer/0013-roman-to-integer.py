class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        valdict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        summ = 0
        prev_val = 0

        for char in s:
            curr_val = valdict[char]
            summ += curr_val
            if curr_val > prev_val:
                summ -= 2 * prev_val
            prev_val = curr_val

        return summ