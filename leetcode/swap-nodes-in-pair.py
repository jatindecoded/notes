# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        prev = dummy
        node1 = head
        node2 = head.next if head else None

        while node1 and node2:
            # save the next pair
            nextPair = node2.next
            
            # change the pointing
            prev.next = node2
            node2.next = node1
            node1.next = nextPair

            # update node1 and node2 and prev
            prev = node1
            node1 = nextPair
            node2 = nextPair.next if nextPair else None
        
        return dummy.next
        



