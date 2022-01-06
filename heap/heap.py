class maxheap:
  
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
    return self.heap

  def delete(self):
    current = 1
    last_index = len(self.heap)-1
        
    self.heap[current] , self.heap[last_index] =  self.heap[last_index] , self.heap[current]
    popped = self.heap.pop()
    
    while(current < last_index):
      left_child = current*2
      right_child = left_child+1
      if(left_child > last_index):
        break
      
      elif(right_child > last_index):
        if(self.heap[left_child] > self.heap[current]):
          self.heap[left_child] , self.heap[current] = self.heap[current] , self.heap[left_child]
          current = left_child
        else:
          break

      else:
        max_index = left_child
        if(self.heap[left_child] < self.heap[right_child]):
            max_index = right_child

        if(self.heap[current] > self.heap[max_index]):
            break
        else:
            self.heap[current] , self.heap[max_index] = self.heap[max_index] , self.heap[current]
            
      return popped
                