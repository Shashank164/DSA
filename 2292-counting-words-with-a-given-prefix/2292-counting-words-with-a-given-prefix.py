class Solution(object):
    def prefixCount(self, words, pref):
        return (sum(wrd[0:len(pref)]==pref for wrd in words)) 
        