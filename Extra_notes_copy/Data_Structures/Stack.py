class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

class Stack:
    def __init__(self):
        self._name = ''
        self._top = None
        self._size = 0

    def is_empty(self) -> bool:
        # if(self._top is None): return True
        # return False
        
        # return size == 0
        return self._top is None
        
    def push(self, data) -> None:
        #created new node
        newNode = Node(data)
        
        #update newNode's next to top and assign top as newNode
        newNode.next = self._top;
        self._top = newNode
        
        self._size += 1
        
    def pop(self) -> any:
        if self.is_empty(): raise Exception('Stack is Empty, cannot pop')
        node_to_delete = self._top
        self._top = self._top.next
        return node_to_delete.data
        
    def test(self):
        node = self._top
        while node is not None:
            print(node.data)
            node = node.next

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

stack.pop()
stack.pop()
stack.pop()

stack.push(5)
stack.push(6)
stack.push(7)

stack.pop()

stack.push(8)
stack.push(9)

stack.test()



# newStack = Stack('my stack')

