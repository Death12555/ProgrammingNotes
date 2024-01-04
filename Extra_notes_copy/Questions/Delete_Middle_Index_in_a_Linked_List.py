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
    
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length= self.get_length(head)
        mid= length//2

        dummy= ListNode(0)
        dummy.next= head
        itr= dummy
        count= 0
        
        while itr:
            if count==mid:
                itr.next= itr.next.next
            
            itr= itr.next
            count+= 1
        
        return dummy.next