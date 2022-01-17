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

  def shiftDown(self, arr, start):
    current = start
    last_index = len(arr) - 1

    while(current < last_index):
      left_child = current*2
      right_child = left_child+1

      #if the index has no child
      if(left_child > last_index):
        break
      
      #if the index has only one child....i.e..left child
      elif(right_child > last_index):
        if(arr[left_child] > arr[current]):
          arr[left_child] , arr[current] = arr[current] , arr[left_child]
        else:
          break
      
      #if the index have both the children
      else:
        max_index = left_child
        if(arr[left_child] < arr[right_child]):
          max_index = right_child

        if(arr[current] > arr[max_index]):
          break
        else:
          arr[current] , arr[max_index] = arr[max_index] , arr[current]
          current = max_index
   
  def delete(self):
    current = 1
    last_index = len(self.heap)-1

    #if the heap is empty
    if(last_index == 0):
      raise Exception("Empty heap")
        
    self.heap[current] , self.heap[last_index] =  self.heap[last_index] , self.heap[current]
    popped = self.heap.pop()

    self.shiftDown(self.heap, 1)
    return popped 

  def heapify(cls, arr):

    for i in range((len(arr)//2) - 1, -1, -1):
      cls.shiftDown(arr, i)
    return arr 
  
  
    