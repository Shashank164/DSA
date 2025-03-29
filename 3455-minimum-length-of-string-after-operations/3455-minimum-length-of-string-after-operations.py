class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        freq = [0 for _ in range(26)]
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        
        for i in range(n):
            if freq[ord(s[i]) - ord('a')] > 2:
                freq[ord(s[i]) - ord('a')] -= 2
        return sum(freq)