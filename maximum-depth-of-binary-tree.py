# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
#         O(n) time and O(logn) space
#         if not root:
#             return 0
#         return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))

#         O(n) time and O(logn) space
        level = 0
        if not root:
            return 0
        stack = []
        stack.append((level, root))
        while stack:
            level,r = stack.pop(0)
            level+=1
            if r.left:
                stack.append((level,r.left))
            if r.right:
                stack.append((level,r.right))
        return level