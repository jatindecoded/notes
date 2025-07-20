# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(head1, head2):
            res = ListNode(-1)
            resPtr = res
            curr1 = head1
            curr2 = head2
            while curr1 or curr2:
                val1 = curr1.val if curr1 else float("inf")
                val2 = curr2.val if curr2 else float("inf")

                if val1 < val2:
                    resPtr.next = curr1
                    resPtr = resPtr.next
                    curr1 = curr1.next
                else:
                    resPtr.next = curr2
                    resPtr = resPtr.next
                    curr2 = curr2.next
            
            return res.next
        
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if i+1 < len(lists) else None

                mergedLists.append(merge(list1, list2))
            lists = mergedLists
        
        return lists[0] if lists else None

       
                    
        




    # def mergeKLists_USING_PRIORITY_QUEUE(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     currNodes  = [(node.val, idx, node) for idx, node in enumerate(lists) if node]
    #     heapq.heapify(currNodes)

    #     dummyHead = ListNode(-1)
    #     ptr = dummyHead

    #     while currNodes:
    #         _, idx, node = heapq.heappop(currNodes)
    #         ptr.next = node
    #         ptr = ptr.next
    #         if node.next:
    #             heapq.heappush(currNodes, (node.next.val, idx, node.next))
        
    #     return dummyHead.next
            
