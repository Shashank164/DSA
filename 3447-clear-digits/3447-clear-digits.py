class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        sb=[]
        for ch in s:            
            if ch.isdigit():
                sb.pop()
            else:
                sb.append(ch)
    
        return "".join(sb)