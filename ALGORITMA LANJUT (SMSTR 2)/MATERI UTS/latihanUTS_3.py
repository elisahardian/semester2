"""
## BUBBLE SORT (asc) (DENGAN CHARCTER)
def bubble_sort(arr):
    arr_len = len(arr)
    for i in range(arr_len - 1):
        flag = 0
        for j in range(0, arr_len - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = 1
                if flag == 0:
                    break
    return arr
arr = ['a', 'z', 'd', 'w', 'b']
print("sebelum di sort: ", arr)
print("bubble sort (asc) (character): ", bubble_sort(arr))

## BUBBLE SORT (asc) (DENGAN DATA INPUT USER)
def bubble_sort(arr):
    arr_len = len(arr)
    for i in range(arr_len - 1):
        flag = 0
        for j in range(0, arr_len - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = 1
                if flag == 0:
                    break
    return arr
arr = []
panjang=int(input("masukkan panjang array: "))
for i in range(panjang):
    elemen=str(input(f"elemen {i+1}: "))
    arr.append(elemen)
print("sebelum di sort: ", arr)
print("bubble sort (asc) (character): ", bubble_sort(arr))
"""
"""
## SEQUENTIAL SEARCH (LINEAR)
def sequential_search(arr, target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i # return index jika target ditemukan
    return -1 # return -1 jika target tidak ditemukan
array = [10, 20, 30, 40, 50, 60]
target = 40
result = sequential_search(array, target)
if result != -1:
    print(f"target ditemukan diindex: {result}")
else:
    print("target tidak ditemukan")

## SEQUENTIAL SEARCH (LINEAR) (dari input user)
def sequential_search(arr, target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i #return index jika target ditemukan
    return -1 #return -1 jika target tidak ditemukan
array=[]
panjang=int(input("masukkan panjang array: "))
for i in range(panjang):
    elemen = int(input(f"elemen {i+1}: "))
    array.append(elemen)
print("sebelum di sort: ", array)
target=int(input("masukkan target: "))
result = sequential_search(array, target)
if result != -1:
    print(f"target ditemukan pada index {result}")
else:
    print("target tidak ditemukan")
"""
"""
## BINARY SEARCH
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        #jika target ditemukan ditengah
        if arr[mid] == target:
            return mid
        #jika terget kurang dari nilai tengah, cari disebelah kiri
        elif target < arr[mid]:
            right = mid - 1
        #jika target lebih besar dari nilai tengah, cari disebelah kanan
        else:
            left = mid + 1
    #jika target tidak ditemukan dalam array
    return -1
array= [2,4,3,6,7,9,0]
target = 9
result = binary_search(array, target)
if result != -1:
    print(f"target ditemukan di index {result}")
else:
    print("target tidak ditemukan")

"""

## INTERPOLATION SEARCH (dengan rekursif)
 
def interpolationSearch(arr, low, high, target):
    # Since array is sorted, an element present
    # in array must be in range defined by corner
    if (low <= high and target >= arr[low] and target <= arr[high]):
        # Probing the position with keeping
        # uniform distribution in mind.
        pos = low + ((high - low) // (arr[high] - arr[low]) * (target - arr[low]))
        # Condition of target found
        if arr[pos] == target:
            return pos
        # If target is larger, target is in right subarray
        if arr[pos] < target:
            return interpolationSearch(arr, pos + 1, high, target)
        # If target is smaller, target is in left subarray
        if arr[pos] > target:
            return interpolationSearch(arr, low, pos - 1, target)
    return -1
 
arr = [10, 12, 13, 16, 18, 19, 20, 21]
n = len(arr)
# Element to be searched
target = 18
index = interpolationSearch(arr, 0, n - 1, target)
if index != -1:
    print("Element found at index", index)
else:
    print("Element not found")
