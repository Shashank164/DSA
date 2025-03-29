class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        n = len(s)
        shift_count = [0] * (n + 1) 
        for start, end, direction in shifts:
            if direction == 1: 
                shift_count[start] += 1
                if end + 1 < n:
                    shift_count[end + 1] -= 1
            else: 
                shift_count[start] -= 1
                if end + 1 < n:
                    shift_count[end + 1] += 1
        current_shift = 0
        result = []
        for i in range(n):
            current_shift += shift_count[i] 
            new_char = chr((ord(s[i]) - ord('a') + current_shift) % 26 + ord('a'))
            result.append(new_char)
        return ''.join(result)