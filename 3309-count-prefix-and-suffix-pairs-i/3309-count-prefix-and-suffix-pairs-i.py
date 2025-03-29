class Solution(object):
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        n=len(words)
        cnt=0        
        for i in range(n):
            for j in range(i+1, n):
                if(words[j].startswith(words[i]) and words[j].endswith(words[i]) ):
                    cnt+=1
                            
        return cnt