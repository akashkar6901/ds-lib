from Node import *

class LinkedList:
  def __init__(self) -> None:
    self.head = None

  def append(self, value):
    new_node = Node(value)

    if(self.head == None):
      self.head = new_node
    else:
      current = self.head
      
      #For finding the last node of the linkedlist.
      while(current.next):
        current = current.next
      current.next = new_node
    
  def traverse(self):
    current = self.head
    
    while(current):
      print(current.value, end="->")
      current = current.next

    print("")

  def insert_at(self, value, index):
    current = self.head
    new_node = Node(value)

    for i in range (index-1):
      if(current.next):
        current = current.next
      else:
        raise Exception ("Index out of range")

    new_node.next = current.next
    current.next = new_node
  
  def delete(self, index):
    current = self.head

    for i in range(index-1):
      if(current.next):
        current = current.next
      else:
        raise Exception ("index out of range")
    current.next = current.next.next

  def middle(self):
    fast=self.head
    slow=self.head

    while(fast and fast.next):
      slow = slow.next
      fast = fast.next.next
    return slow.value
  
  def is_cyclic(self):
    if(self.head == None):
      return False
    else:

      fast = self.head.next
      slow = self.head

      while (fast and fast.next):
        if(slow == fast):
          return True
        fast = fast.next.next
        slow = slow.next
      return False