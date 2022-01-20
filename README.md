# DS-LIBRARY
- A Data Structure Library which consist of multiple common DS and there implementation
## LinkedList
    ### methods:
        - append(value)  : pass the value to be inserted at end of LinkedList
        - iterate() : Loops over the linked list
        - delete(index) : pass the index of node which has to be deleted
        - middle()  : returns the value of middle node
        - reverse() : reverse the linkedlist
        - isCyclic() : checks whether there is a cycle or not

    example:
        ```
    l1 = LinkedList()
    l1.append(1)
    l1.append('xyz')
    l1.append(True)
    l1.traverse() // -> 1->xyz->True
    l1.reverse() // _> True->xyz->1
    l1.middle() // -> xyz
    l1.isCycle // False

    ```
## STACK
    ### methods:
        - push(value) : pass the value to be inserted in stack
        - pop() : deletes the last element inserted in the stack
        - peek() : returns the top element
## HEAP
    ### methods :
        - insert(value) : pass the value to be inserted in heap
        - delete() : deletes the head of the heap
        - heapify(array) : pass the array and it will return the heapified array.
### SORTING
    BUBBLE SORT :
        We will pass an array and it will returns the sorted array using Bubble Sort method.
        
    
