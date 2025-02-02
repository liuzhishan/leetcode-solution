# -*- coding: utf-8 -*-

from typing import List, Optional

from tool import ListNode


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head == None or left > right:
            return head

        dummy = ListNode(0, head)
        pre = dummy
        cur = head

        for i in range(1, left):
            pre = pre.next
            cur = cur.next

        start = pre
        end = cur

        for i in range(left, right + 1):
            next = cur.next
            cur.next = start
            start = cur
            cur = next
        
        pre.next = start
        end.next = cur

        return dummy.next
