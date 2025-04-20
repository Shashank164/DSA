class Solution:
    def numRabbits(self, answers):
        from collections import Counter
        count = Counter(answers)
        res = 0
        for a, freq in count.items():
            group_size = a + 1
            groups = (freq + a) // group_size 
            res += groups * group_size
        return res