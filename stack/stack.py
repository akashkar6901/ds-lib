class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
     
class Stack:
    def __init__(self):
        self.top = None

    def push(self,data):
        new_node = Node(data)
         
        if self.top == None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if (self.top == None):
            raise Exception("underflow")
        else:
            current = self.top
            self.top = self.top.next
            return current.data

    def peek(self):
        if self.top == None:
            raise Exception("empty stack")
        else:
            return self.top.data