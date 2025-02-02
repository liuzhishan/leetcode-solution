# -*- coding: utf-8 -*-

from typing import List, Optional

from tool import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True

        limit = 2 ** 31
        return self.isValid(root, -limit, limit - 1)

    def isValid(self, root: Optional[TreeNode], min_val: int, max_val: int) -> bool:
        if root == None:
            return True

        if root.val <= max_val and root.val >= min_val:
            return self.isValid(root.left, min_val, root.val - 1) and self.isValid(root.right, root.val + 1, max_val)
        else:
            return False