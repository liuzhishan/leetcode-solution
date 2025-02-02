# -*- coding: utf-8 -*-

from typing import List, Optional

from tool import TreeNode


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []

        nums = [i for i in range(1, n + 1)]
        res = self.generate(nums, 0, n - 1)

        return res

    def generate(self, nums: List[int], left: int, right: int) -> List[Optional[TreeNode]]:
        if left > right:
            return [None]
        
        res = []

        for i in range(left, right + 1):
            left_trees = self.generate(nums, left, i - 1)
            right_trees = self.generate(nums, i + 1, right)

            for x in left_trees:
                for y in right_trees:
                    root = TreeNode(nums[i])
                    root.left = x
                    root.right = y
                    res.append(root)
        
        return res
