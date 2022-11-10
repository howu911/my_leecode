# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        value_l = []
        def Traverse(root):
            if root is None:
                return
            value_l.append(root.val)
            Traverse(root.left)
            Traverse(root.right)
        
        Traverse(root)
        return value_l