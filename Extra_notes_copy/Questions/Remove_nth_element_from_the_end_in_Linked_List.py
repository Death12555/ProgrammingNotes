# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def get_length(self, head):
        count= 0
        
        itr= head
        while itr:
            count+= 1
            itr= itr.next
        return count
    

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length= self.get_length(head)
        if n<0 or n>self.get_length(head):
            raise Exception("Invalid Index")
            return

        dummy= ListNode(0)
        dummy.next= head
        itr= dummy

        for i in range(length-n):
            itr= itr.next
            
        itr.next= itr.next.next
        
        return dummy.next