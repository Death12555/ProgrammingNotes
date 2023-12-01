class Node:
    def __init__(self, data):
        self.data= data
        self.next= None
    
class Queue:
    def __init__(self):
        self.front= None
        self.rear= None
    
    def isEmpty(self):
        return self.front is None

    def enqueue(self, data):
        new_node= Node(data)
        
        if self.isEmpty():
            self.front= self.rear= new_node
        
        else:
            self.rear.next= new_node
            self.rear= new_node

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty.")
        
        data= self.front.data
        self.front= self.front.next
        
        if self.front is None:
            self.rear= None
        
    def print_queue(self):
        itr= self.front
        
        while itr:
            print(itr.data, end= " ")
            itr= itr.next
            

if __name__== '__main__':
    queue= Queue()
    queue.enqueue(78)
    queue.enqueue(765)
    queue.enqueue(765)
    queue.enqueue(234)
    queue.enqueue(67)
    queue.enqueue(98)
    queue.print_queue()
    queue.dequeue()
    queue.print_queue()
    queue.enqueue(34)
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.print_queue()