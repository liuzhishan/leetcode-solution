# -*- coding: utf-8 -*-

from typing import List, Optional, Tuple

from tool import TreeNode


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return

        self.pre = None
        self.x = None
        self.y = None

        self.inorder(root)

        if self.x != None and self.y != None:
            self.x.val, self.y.val = self.y.val, self.x.val

    def inorder(self, root: Optional[TreeNode]) -> None:
        if root == None:
            return

        self.inorder(root.left)

        if self.pre == None:
            self.pre = root
        else:
            if self.pre.val < root.val:
                self.pre = root
            else:
                self.y = root
                if self.x == None:
                    self.x = self.pre
                self.pre = root

        self.inorder(root.right)
