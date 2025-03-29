class Solution(object):
   
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        n=len(words)
        res = []

        def checkSubstring(words, idx, subStr, n):
            for j in range(n):
                if i==j: 
                    continue
                if subStr in words[j]:
                    return True

            return False

        for i in range(n):
            if checkSubstring(words, i, words[i], n):
                res.append(words[i])
        

        return res
                      