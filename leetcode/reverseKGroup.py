# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''


'''
def findNewTail(prevTail, k): # return newTail
    # initialise variables
    start = prevTail.next

    prev = prevTail
    curr = start

    # reverse pointers
    for _ in range(k):
        nextOfCurr = curr.next
        curr.next = prev
        prev = curr
        curr = nextOfCurr
    
    # end = prev
    prevTail.next = prev 
    start.next = curr
    
    return start

def enoughNodes(ptr, k):
    for _ in range(k):
        if not ptr:
            return False
        ptr = ptr.next
    
    return True
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(-1, head)

        tail = dummy

        while tail:
            if not enoughNodes(tail.next, k):
                break
            print(f"{tail=}")
            tail = findNewTail(tail, k)
        
        return dummy.next
                