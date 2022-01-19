def BubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swap = 0
        for j in range(n-1):
            if(arr[j] < arr[j+1]):
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
                swap += 1
        if(swap == 0):
            break
    return arr
    
arr = list(map(int,input("ENTER THE ARRAY:-").split(" ")))
print(BubbleSort(arr))
