# -*- coding: utf-8 -*-

import logging
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        cur = dummy

        while cur.next != None and cur.next.next != None:
            first = cur.next
            second = cur.next.next

            first.next = second.next
            second.next = first

            cur.next = second
            cur = first

        return dummy.next
