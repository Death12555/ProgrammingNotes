class Node:
    def __init__(self, data= None, next= None):
        self.data= data
        self.next= next
        
class Linked_List:
    def __init__(self):
        self.head= None
        
    def insert_at_beginning(self, data):
        new_node= Node(data, self.head)
        self.head= new_node
        
    def get_length(self):
        count= 0
        itr= self.head
        
        while itr:
            itr= itr.next
            count+= 1
        
        return count
    
    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")
            return
        
        count= 0
        itr= self.head
        
        if index==0:
            self.insert_at_beginning(data)
        
        while itr:
            if count==index-1:
                itr.next= Node(data, itr.next)
            
            itr= itr.next
            count+= 1
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head= Node(data, self.head)
            
        itr= self.head
        while itr.next:
            itr= itr.next
        itr.next= Node(data, None)
            
    def remove_at(self, index):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")
            return
        
        count= 0
        itr= self.head
        while itr:
            if count==index-1:
                itr.next= itr.next.next
            itr= itr.next
            count+= 1
    
    def update_node(self, index, new_data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")
            return -1
        if index==0:
            self.head.data= new_data
        
        count= 0
        itr= self.head
        while itr:
            if count==index:
                itr.data= new_data
            itr= itr.next
            count+= 1
    
    def print_list(self):
        if self.head is None:
            print("List is Empty")
        itr= self.head
        ll_string= ''
        
        while itr:
            ll_string+= str(itr.data) + '-->'
            itr= itr.next
        print(ll_string)

if __name__== '__main__':
    ll= Linked_List()
    ll.print_list()
    ll.insert_at_beginning(32)
    ll.insert_at_beginning(12)
    ll.insert_at_beginning(34)
    ll.insert_at_beginning(45)
    ll.print_list()
    ll.insert_at_end(100)
    ll.insert_at_end(65)
    ll.insert_at_end(785)
    ll.insert_at_end(345)
    ll.insert_at_end(123)
    ll.print_list()
    ll.remove_at(2)
    ll.print_list()
    ll.insert_at(2, 67)
    ll.print_list()
    ll.update_node(4, 69)
    ll.print_list()