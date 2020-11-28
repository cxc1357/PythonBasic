def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j] 

def selectSort(arr):
    n = len(arr)
    for i in range(n):
        minIndex = i
        for j in range(i+1,n):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]    

def insertionSort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

if __name__ == "__main__":
    a = [1,4,3,5,2]
    #bubbleSort(a)
    #selectSort(a)
    insertionSort(a)
    print(a)

