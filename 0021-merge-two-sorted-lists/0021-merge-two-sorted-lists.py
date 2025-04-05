class Solution:
    def mergeTwoLists(self, a, b):
        if not a or (b and a.val > b.val):
            a, b = b, a
        if a:
            a.next = self.mergeTwoLists(a.next, b)
        return a