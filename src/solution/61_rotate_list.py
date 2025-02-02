# -*- coding: utf-8 -*-

from typing import List, Optional

from tool import ListNode

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return head

        n = 0
        cur = head
        while cur != None:
            n += 1
            cur = cur.next
        
        k %= n
        if k == 0:
            return head

        cur = head
        for _ in range(n - k - 1):
            cur = cur.next

        new_head = cur.next
        cur.next = None

        cur = new_head
        while cur.next != None:
            cur = cur.next

        cur.next = head

        return new_head