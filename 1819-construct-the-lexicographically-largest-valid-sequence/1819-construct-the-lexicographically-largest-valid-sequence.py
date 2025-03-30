class Solution(object):
    def constructDistancedSequence(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        size = 2 * n - 1  
        res = [0] * size  
        used = set()  
        
        def backtrack(index):
            if index == size:
                return True
            
            if res[index] != 0:
                return backtrack(index + 1)
            
            for num in range(n, 0, -1):
                if num in used:
                    continue  
                
                if num > 1:
                    if index + num >= size or res[index + num] != 0:
                        continue  
                
                res[index] = num
                if num > 1:
                    res[index + num] = num
                used.add(num)

                if backtrack(index + 1):
                    return True  
                
                res[index] = 0
                if num > 1:
                    res[index + num] = 0
                used.remove(num)

            return False  
        
        backtrack(0)
        return res