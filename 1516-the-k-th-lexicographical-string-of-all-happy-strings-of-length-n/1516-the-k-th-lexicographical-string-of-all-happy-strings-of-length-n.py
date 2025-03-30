class Solution(object):
    def getHappyString(self, n, k):
        def backtrack(s, last_char):
            if len(s) == n:
                self.count += 1
                if self.count == k:
                    self.result = s
                return

            for c in "abc":
                if c != last_char:
                    backtrack(s + c, c)
                    if self.result:
                        return

        self.count = 0
        self.result = ""
        backtrack("", "")
        return self.result