class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        prefix = min(strs, key=len)
        for string in strs:
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix