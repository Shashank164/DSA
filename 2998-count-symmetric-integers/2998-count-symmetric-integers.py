class Solution(object):
    def countSymmetricIntegers(self, low, high):
       
        count = 0
        for num in range(low, high + 1):
            if self.is_symmetric(num):
                count += 1
        return count
    
    def is_symmetric(self, num):
        s = str(num)
        length = len(s)
        
        # Numbers with odd digits can't be symmetric
        if length % 2 != 0:
            return False
        
        half = length // 2
        first_half_sum = sum(int(d) for d in s[:half])
        second_half_sum = sum(int(d) for d in s[half:])
        
        return first_half_sum == second_half_sum