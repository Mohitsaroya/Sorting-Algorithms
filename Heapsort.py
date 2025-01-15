def heapsort(arr):
    n = len(arr)
    buildheapmax(arr, n)
    
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)
    return arr
    
def buildheapmax(arr, n):
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, i, n)

def heapify(arr, i, n):
    largest = i
    left = 2*i + 1
    right = 2*i + 20
    
    if left < n and arr[left] > arr[i]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, largest, n)
    
arr = [0, 64, 34, 25, 12, 22, 11, 90]
print(heapsort(arr))