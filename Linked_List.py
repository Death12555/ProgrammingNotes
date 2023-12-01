

# Online Python - IDE, Editor, Compiler, Interpreter

class Node:

    def __init__(self, data=None, next=None):
        self.data= data
        self.next= next


class Linked_List:
    def __init__(self):
        self.head= None
    
    def insert_at_beginning(self, data):
        new_node= Node(data, self.head)
        self.head= new_node
    
    def print_list(self):
        if self.head is None:
            print("List is Empty")
            return

        itr= self.head
        llstr= ''
        while itr:
            llstr+= str(itr.data) + '-->'
            itr= itr.next
        print(llstr)
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head= Node(data, None)
            return
        
        itr= self.head
        while itr.next:
            itr= itr.next
        itr.next= Node(data, None)
    
    def insert_values(self, data_list):
        self.head= None
        for data in data_list:
            self.insert_at_end(data)
    
    def get_length(self):
        count= 0
        
        itr= self.head
        while itr:
            count+= 1
            itr= itr.next
        return count
    
    def remove_at(self, index):
        if index<0 or index>self.get_length():
            raise Exception("Invalid index")
        
        if index==0:
            self.head= self.head.next
            return
        
        count= 0
        itr= self.head
        while itr:
            if count== index-1:
                itr.next= itr.next.next
                return
            
            itr= itr.next
            count+= 1
    
    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invaild index")
        
        if index==0:
            self.insert_at_beginning(data)
            return
        
        count= 0
        itr= self.head
        while itr:
            if count== index-1:
                itr.next= Node(data, itr.next)
                return
            
            itr= itr.next
            count+= 1
    
    def update_node(self, index, new_data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")
        
        if index==0:
            self.head.data= new_data
        
        itr= self.head
        count= 0
        while itr:
            if count==index:
                itr.data= new_data
                return
            itr= itr.next
            count+= 1
    
    def reverse_list(self):
        prev= None
        curr= self.head
        
        while curr:
            next_temp= curr.next
            curr.next= prev
            prev= curr
            curr= next_temp
            
            self.head= prev
            
        return prev
    
        def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        
        slow= head
        fast= head.next
        
        while slow!= fast:
            if fast is None or fast.next is None:     #Using two pointers, slow and fast pointers to check the nodes instead of using a hash table to check the same thing makes space complexity go down from O(n) to O(1)
                return False
            
            slow= slow.next
            fast= fast.next.next
        
        return True
        
        def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow= fast= head

        # Phase 1: Determine if there is a cycle
        while fast and fast.next:
            slow= slow.next
            fast= fast.next.next

            if slow==fast:
                # There is a cycle, move to phase 2
                break
        else:
            # No cycle found
            return None

        # Phase 2: Find the node where the cycle starts
        slow= head
        while slow!= fast:
            slow= slow.next
            fast= fast.next

        return slow


if __name__== '__main__':
    ll= Linked_List()
    ll.insert_at_beginning(56)
    ll.insert_at_beginning(90)
    ll.insert_at_beginning(100)
    ll.print_list()
    ll.insert_at_end(67)
    ll.insert_at_end(92)
    ll.insert_at_end(36)
    ll.print_list()
    ll.insert_values([34, 78, 89, 675])
    ll.print_list()
    ll.insert_at(3, 85)
    ll.print_list()
    ll.remove_at(4)
    ll.print_list()
    ll.update_node(2, 64)
    ll.print_list()
    ll.reverse_list()
    ll.print_list()
    
