class FindElements(object):
    
    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.sets = set()
        if root:
            root.val = 0
            self.recover(root)

    def recover(self, node):
        if node:
            self.sets.add(node.val)
            if node.left:
                node.left.val = 2 * node.val + 1
                self.recover(node.left)
            if node.right:
                node.right.val = 2 * node.val + 2
                self.recover(node.right)

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        return target in self.sets