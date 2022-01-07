class MaxHeap:
  def __init__(self):
    self.heap = [None]
    
  def insert(self,value):
    self.heap.append(value)
    current = len(self.heap)-1

    while(current > 1):
      parent=current//2
      if(self.heap[parent] < self.heap[current]):
        self.heap[parent] , self.heap[current] = self.heap[current] , self.heap[parent]
        current = parent
      else:
        break
    
  def delete(self):
    current = 1
    last_index = len(self.heap)-1

    #if the heap is empty
    if(last_index == 0):
      raise Exception("Empty heap")
        
    self.heap[current] , self.heap[last_index] =  self.heap[last_index] , self.heap[current]
    popped = self.heap.pop()
    last_index -=1
    
    while(current < last_index):
      left_child = current*2
      right_child = left_child+1

      #if the index has no child
      if(left_child > last_index):
        break
      
      #if the index has only one child....i.e..left child
      elif(right_child > last_index):
        if(self.heap[left_child] > self.heap[current]):
          self.heap[left_child] , self.heap[current] = self.heap[current] , self.heap[left_child]
        else:
          break
      
      #if the index have both the children
      else:
        max_index = left_child
        if(self.heap[left_child] < self.heap[right_child]):
          max_index = right_child

        if(self.heap[current] > self.heap[max_index]):
          break
        else:
          self.heap[current] , self.heap[max_index] = self.heap[max_index] , self.heap[current]
          current = max_index

    return popped                