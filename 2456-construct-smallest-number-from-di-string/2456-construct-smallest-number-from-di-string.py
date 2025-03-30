class Solution(object):
    def smallestNumber(self, s):
        res, stack = [], []
        for i, c in enumerate(s + 'I', 1):
            stack.append(str(i))
            if c == 'I':
                res.extend(stack[::-1])
                stack = []
        return ''.join(res)