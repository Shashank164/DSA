class Solution(object):
    def isValid(self, s):
        opcl = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for char in s:
            if char in opcl:
                stack.append(char)
            elif not stack or opcl[stack.pop()] != char:
                return False
        return not stack