# -*- coding: utf-8 -*-

import logging
from typing import Optional

logging.basicConfig(level=logging.INFO, format="[%(filename)s:%(lineno)s - %(funcName)s] - %(message)s")


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2
        root = ListNode(0)
        flag = 0

        node = root
        while p1 and p2:
            node.next = ListNode((p1.val + p2.val + flag) % 10)
            node = node.next

            flag = (p1.val + p2.val + flag) // 10
            p1 = p1.next
            p2 = p2.next

        while p1 != None:
            node.next = ListNode((p1.val + flag) % 10)
            node = node.next
            flag = (p1.val + flag) // 10
            p1 = p1.next

        while p2 != None:
            node.next = ListNode((p2.val + flag) % 10)
            node = node.next
            flag = (p2.val + flag) // 10
            p2 = p2.next

        if flag != 0:
            node.next = ListNode(flag)
            node = node.next

        return root.next


def run():
    pass


if __name__ == "__main__":
    run()