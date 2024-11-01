##https://leetcode.com/problems/binary-tree-right-side-view/?envType=study-plan-v2&envId=leetcode-75

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        lis = []
        level  = 0
        self.dfs(root,lis,level)
        return lis
        
    def dfs(self, node, li , level):
        if not node:
            return None
        
        if len(li) == level:
            li.append(node.val)

        self.dfs(node.right, li, level + 1)
        self.dfs(node.left, li, level + 1)
        
        