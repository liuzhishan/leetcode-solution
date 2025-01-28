# -*- coding: utf-8 -*-

import logging
from typing import Optional, List


from tool import ListNode, nested_list_to_nodes, nodes_to_list


class Solution:
    def heapify(self, heap: List[ListNode]):
        n = len(heap)
        for i in range(n):
            self.heapifyUp(heap, i)

    def heapifyUp(self, heap: List[ListNode], i: int):
        while i > 0:
            parent = (i - 1) // 2
            if heap[parent].val >= heap[i].val:
                heap[parent], heap[i] = heap[i], heap[parent]
                i = parent
            else:
                break

    def popHeap(self, heap: List[ListNode]) -> Optional[ListNode]:
        n = len(heap)
        if n == 0:
            return None

        heap[0], heap[n - 1] = heap[n - 1], heap[0]

        i = 0
        while i < n - 1:
            left = 2 * i + 1
            right = 2 * i + 2

            if left >= n - 1:
                break

            if right >= n - 1:
                if left < n - 1 and heap[left].val <= heap[i].val:
                    heap[i], heap[left] = heap[left], heap[i]
                    i = left
                else:
                    break
            elif heap[i].val <= heap[left].val and heap[i].val <= heap[right].val:
                break
            elif heap[left].val <= heap[i].val and heap[left].val <= heap[right].val:
                heap[i], heap[left] = heap[left], heap[i]
                i = left
            elif heap[right].val <= heap[i].val and heap[right].val <= heap[left].val:
                heap[i], heap[right] = heap[right], heap[i]
                i = right
            else:
                break

        return heap.pop()

    def pushHeap(self, heap: List[ListNode], node: Optional[ListNode]):
        heap.append(node)
        self.heapifyUp(heap, len(heap) - 1)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        heap = []

        for i in range(k):
            if lists[i] != None:
                heap.append(lists[i])

        self.heapify(heap)
        n = len(heap)

        dummy = ListNode()
        cur = dummy

        while len(heap) > 0:
            node = self.popHeap(heap)
            if node == None:
                break

            cur.next = node
            cur = cur.next

            if cur.next != None:
                self.pushHeap(heap, cur.next)

        return dummy.next


def run():
    lists = [[-3,2,2],[-9],[-10,-5,-4,-2,-1,1,3,4],[-10,-9,-8,3,4],[-5,-3,3,4],[-9,-8,-5,-4,-2,-1,3]]
    nodes = nested_list_to_nodes(lists)

    solution = Solution()
    res = solution.mergeKLists(nodes)
    logging.info("res: %s", nodes_to_list(res))


if __name__ == "__main__":
    run()
