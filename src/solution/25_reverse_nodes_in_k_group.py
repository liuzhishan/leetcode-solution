# -*- coding: utf-8 -*-

import logging
from typing import Optional, List

from tool import ListNode, list_to_nodes, nodes_to_list


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        cur = dummy

        sub = cur.next
        next_sub = sub

        pre = dummy
        cur = dummy.next
        last = dummy.next

        cnt = 0
        while cur != None:
            cnt += 1

            if cnt == k:
                cur_next = cur.next
                cur.next = sub
                pre.next = cur

                last.next = cur_next

                cur = cur_next
                pre = last

                last = cur_next
                cnt = 0

                if last != None:
                    sub = last.next
            else:
                cur_next = cur.next
                cur.next = sub
                sub = cur
                cur = cur_next

                if cnt == 1:
                    last.next = None

        if cnt > 0 and cnt < k:
            new_cnt = 0
            new_cur = sub
            last = sub
            while new_cur != None:
                cur_next = new_cur.next
                new_cur.next = sub
                sub = new_cur
                new_cur = cur_next

                new_cnt += 1
                if new_cnt == 1:
                    last.next = None

            pre.next = sub

        return dummy.next


def run():
    lists = [1,2,3,4,5]
    k = 2
    
    solution = Solution()
    res = solution.reverseKGroup(list_to_nodes(lists), k)
    logging.info("res: %s", nodes_to_list(res))


if __name__ == "__main__":
    run()
