# -*- coding: utf-8 -*-

from typing import List, Optional

from tool import ListNode


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head == None:
            return head
        
        small = ListNode(0)
        large = ListNode(0)

        small_head = small
        large_head = large

        cur = head
        while cur != None:
            if cur.val < x:
                small_head.next = cur
                small_head = small_head.next
            else:
                large_head.next = cur
                large_head = large_head.next

            cur = cur.next

        small_head.next = large.next
        large_head.next = None

        return small.next