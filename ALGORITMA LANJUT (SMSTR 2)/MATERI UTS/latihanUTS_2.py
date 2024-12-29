"""
## BUBBLE SORT (ASCENDING)
def bubble_sort(arr):
    arr_len = len(arr)
    for i in range(arr_len -1):
        flag = 0
        for j in range(0, arr_len-i-1):
            if arr[j]>arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                flag = 1
                if flag == 0:
                    break
    return arr
arr=[5,3,4,1,2]
print("array sebelum di sort: ", arr)
print("Bubble sort (arc): ", bubble_sort(arr))

print()
## BUBBLE SORT (DESCENDING)
def bubble_sort(arr):
    arr_len = len(arr)
    for i in range(arr_len - 1):
        flag = 0
        for j in range(0, arr_len - i - 1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = 1
                if flag == 0:
                    break
    return arr
arr = [5,3,4,1,2]
print("array sebelum di sort: ", arr)
print("Bubble sort (desc): ", bubble_sort(arr))

print()
## SELECTION SORT (ASCENDING)
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1 , n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(arr)
arr = [64, 34, 25, 12, 11, 90]
print("array sebelum di sort: ", arr)
print("--sorting--")
selection_sort(arr)
print("--selesai--")
print("Selection sort (asc): ", arr)

print()
## SELECTION SORT (DESCENDING)
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] > arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(arr)
arr = [64, 34, 25, 12, 11, 90]
print("array sebelum di sort: ", arr)
print("--sorting--")
selection_sort(arr)
print("--selesai--")
print("Selection sort (desc): ", arr) 
"""
"""
print()
## INSERTION SORT (ASCENDING)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    print("Insertion sort (asc): ", arr)
arr = [64, 34, 25, 12, 11, 90]
print("array sebelum di sort: ", arr)
insertion_sort(arr)

print()
## INSERTION SORT (DESCENDING)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    print("Insertion sort (desc): ", arr)
arr = [64, 34, 25, 12, 11, 90]
print("array sebelum di sort: ", arr)
insertion_sort(arr)

print()
## QUICK SORT (ASCENDING)
def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i+1], array[high]) = (array[high], array[i+1])
    return i+1
def quicksort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quicksort(array, low, pi-1)
        quicksort(array, pi+1, high)
data= [64, 34, 25, 12, 11, 90]
size = len(data)
print("array sebelum di sort: ", data)
quicksort(data, 0, size-1)
print("Quick sort (asc): ", data)

print()
## QUICK SORT (DESCENDING)
def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] >= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i+1], array[high]) = (array[high], array[i+1])
    return i+1
def quicksort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quicksort(array, low, pi-1)
        quicksort(array, pi+1, high)
data= [64, 34, 25, 12, 11, 90]
size = len(data)
print("array sebelum di sort: ", data)
quicksort(data, 0, size-1)
print("Quick sort (desc): ", data)
"""

print()
## MERGE SORT (ASCENDING)
def merge(list, reverse=False):
    if len(list)<2:
        return list
    middle = len(list)//2
    left = merge(list[:middle], reverse)
    right = merge(list[middle:], reverse)
    i, j, k = 0, 0, 0
    if reverse:
        while i < len(left) and j < len(right):
            if left[i] >= right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += i
            k += 1
        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1
    else:
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                list[k] = left[i]
                i+=1
            else:
                list[k]= right[j]
                j+=1
            k+=1
        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1
    return list
list = [64, 34, 25, 12, 11, 90]
print("array sebelum di sort: ", list)
print("Merge sort (asc): ", end= " ")
print(merge(list, reverse = False))

print()
## MERGE SORT (DESCENDING)
def merge(list, reverse=False):
    if len(list)<2:
        return list
    middle = len(list)//2
    left = merge(list[:middle], reverse)
    right = merge(list[middle:], reverse)
    i, j, k = 0, 0, 0
    if reverse:
        while i<len(left) and j<len(right):
            if left[i]>= right[j]:
                list[k] = left[i]
                i +=1
            else:
                list[k] = right[j]
                j+=1
            k+=1
        while i < len(left):
            list[k] = left[i]
            i+=1
            k+=1
        while j< len(right):
            list[k]=right[j]
            j+=1
            k+=1
    else:
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                list[k] = left[i]
                i+=1
            else:
                list[k]= right[j]
                j+=1
            k+=1
        while i < len(left):
            list[k] = left[i]
            i+=1
            k+=1
        while j < len(right):
            list[k]=right[j]
            j+=1
            k+=1
    return list
list = [64, 34, 25, 12, 11, 90]
print("array sebelum di sort: ", list)
print("Merge sort (desc): ", end=" ")
print(merge(list, reverse = True))
