class Solution(object):
    def wordSubsets(self, words1, words2):
        res=[]
        max1=[0]*26
        for char in words2:
            freq=[0]*26
            for c in char:
                freq[ord(c)-ord('a')]+=1
            for i in range(26):
                max1[i]=max(max1[i],freq[i])
        for word in words1:
            freq=[0]*26
            for ch in word:
                freq[ord(ch)-ord('a')]+=1
            ispal=True
            for i in range(26):
                if freq[i]<max1[i]:
                    ispal=False
                    break
            if ispal:
                res.append(word)
        return res
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        