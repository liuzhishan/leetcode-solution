# -*- coding: utf-8 -*-

import logging
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None:
            return None

        dummy = ListNode(0, head)

        total = 0
        cur = dummy

        while cur.next != None:
            cur = cur.next
            total += 1

        target = total - n

        new_total = 0
        cur = dummy
        while cur != None:
            if new_total == target:
                if cur.next != None:
                    cur.next = cur.next.next
                else:
                    cur.next = None
                break

            cur = cur.next
            new_total += 1

        return dummy.next
