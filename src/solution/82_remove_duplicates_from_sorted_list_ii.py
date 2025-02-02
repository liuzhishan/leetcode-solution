# -*- coding: utf-8 -*-

from typing import List, Optional

from tool import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        dummy = ListNode(0, head)

        pre = dummy
        cur = dummy.next

        while cur != None:
            count_node = 1
            while cur.next != None and cur.val == cur.next.val:
                count_node += 1
                cur = cur.next

            if count_node == 1:
                pre.next = cur
                cur = cur.next
                pre = pre.next
            else:
                pre.next = cur.next
                cur = cur.next

        return dummy.next