# -*- coding: utf-8 -*-

from typing import List, Optional

from tool import TreeNode


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.traverse(root, res)
        return res

    def traverse(self, root: Optional[TreeNode], res: List[int]) -> None:
        if root == None:
            return
        
        self.traverse(root.left, res)
        res.append(root.val)
        self.traverse(root.right, res)