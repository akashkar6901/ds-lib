def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swap_count = 0
        for j in range(n-1):

            if(arr[j] < arr[j+1]):
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
                swap_count += 1

        if(swap_count == 0):
            #that means the array is already sorted so break the loop.
            break
    return arr
    
arr = list(map(int,input("ENTER THE ARRAY:-").split(" ")))
print(bubble_sort(arr))
