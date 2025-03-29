class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        result = []
        freq = [0] * (len(A) + 1)
        c = 0
        for i in range(len(A)):
            freq[A[i]] += 1
            if (freq[A[i]] == 2):
                c += 1
            freq[B[i]] += 1
            if (freq[B[i]] == 2):
                c += 1
            result.append(c)
        return result

