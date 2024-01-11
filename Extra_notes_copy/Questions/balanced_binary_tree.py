# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):

        def check_height(node):
            if node is None:
                return 0
            left_h, right_h= check_height(node.left), check_height(node.right)
        
            if left_h<0 or right_h<0 or abs(left_h-right_h)>1:
                return -1
        
            return max(left_h, right_h) + 1

        return check_height(root)>=0