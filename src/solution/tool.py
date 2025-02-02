# -*- coding: utf-8 -*-

import logging
from typing import Optional, List


LOG_FORMAT = "%(asctime)s - %(levelname)s [%(filename)s:%(lineno)s - %(funcName)s] - %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
logger = logging.getLogger(__name__)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def nested_list_to_nodes(lists: List[List[int]]) -> List[ListNode]:
    res = []

    for x in lists:
        nodes = []
        for y in x:
            nodes.append(ListNode(y))

        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]

        if len(nodes) > 0:
         res.append(nodes[0])

    return res


def nodes_to_list(node: Optional[ListNode]) -> List[int]:
    res = []

    while node != None:
        res.append(node.val)
        node = node.next

    return res


def list_to_nodes(lists: List[int]) -> ListNode:
    dummy = ListNode()
    cur = dummy 

    for x in lists:
        cur.next = ListNode(x)
        cur = cur.next

    return dummy.next