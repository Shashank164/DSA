# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        result = ListNode(0)
        current = result
        overhead = 0

        while l1 or l2 or overhead:
            x1 = l1.val if l1 else 0
            x2 = l2.val if l2 else 0
            total = x1 + x2 + overhead
            overhead = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return result.next