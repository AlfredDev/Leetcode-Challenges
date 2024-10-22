from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        cola = deque([root])
        levelsSum = []
        while cola:
            size = len(cola)
            sum = 0
            for i in range(size):
                node = cola.popleft()
                sum += node.val
                if node.left:
                    cola.append(node.left)
                if node.right:
                    cola.append(node.right)
            levelsSum.append(sum)
        levelsSum.sort(reverse=True)
        if k <= len(levelsSum):
            return levelsSum[k - 1]

        return -1
