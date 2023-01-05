def SortSelection(arr):
    for i in range(len(arr)-1):
        minIndex = i
        for j in range(i+1,len(arr)):
            if arr[minIndex] > arr[j]:
                minIndex = j
        arr[minIndex],arr[i] = arr[i],arr[minIndex]
    return arr
# arr = [29,72,98,13,87,66,52,51,36]
# print(SortSelection(arr))

def SortBubble(arr):
    n = len(arr)
    swapped = False
    for i in range(1,n):
        for j in range(0,n-i):
            if arr[j] > arr[j+1]:
                arr[j+1],arr[j] = arr[j],arr[j+1]
                swapped = True
        if swapped == False:
            break
    return arr
# arr = [5,4,3,2]
# print(SortBubble(arr))

def SortInsertion(arr):
    n = len(arr)
    i = 1
    while i<n:
        temp = arr[i]
        j = i-1
        while j>=0:
            if arr[j]>temp:
                arr[j+1] = arr[j]
            else:
                break
            j-=1
        arr[j+1] = temp
        i+=1
    return arr
# arr = [5,4,1,2]
# print(SortInsertion(arr))

def merge(arr,start,end):
    '''merge two arrays while sorting them'''
    mid = start + (end-start)//2
    len1 = mid - start + 1
    len2 = end-mid
    first = [0]*len1
    second = [0]*len2

    # split main array into two subarrays
    ArrIndex = start
    for i in range(len1):
        first[i] = arr[ArrIndex]
        ArrIndex+=1
    ArrIndex = mid+1
    for i in range(len2):
        second[i] = arr[ArrIndex]
        ArrIndex+=1

    # merge two arrays
    index1 = 0
    index2 = 0
    ArrIndex = start
    while index1 < len1 and index2 < len2:
        if first[index1] < second[index2]:
            arr[ArrIndex] = first[index1]
            index1+=1
        else:
            arr[ArrIndex] = second[index2]
            index2+=1
        ArrIndex+=1
    
    while index1 < len1:
        arr[ArrIndex] = first[index1]
        ArrIndex+=1
        index1+=1
    while index2<len2:
        arr[ArrIndex] = second[index2]
        ArrIndex+=1
        index2+=1
    return arr
    

def mergeSort(arr,start,end):
    '''Use of merge sort algorothm'''
    # base case
    if start>=end:
        return arr
    # processing
    mid = start+(end-start)//2
    # left part recursion
    mergeSort(arr,start,mid)
    # right part recursion
    mergeSort(arr,mid+1,end)

    # merge 
    return merge(arr,start,end)
# arr = [8,5,1,7,3]
# print(mergeSort(arr,0,len(arr)-1))

def partition(arr,start,end):
    '''place pivot element to its right place'''
    pivot = arr[start]
    cnt = 0
    for i in range(start+1,end+1):
        if arr[i]<=pivot:
            cnt+=1
    
    # pivot place
    pivotIndex = start + cnt
    arr[pivotIndex],arr[start] = arr[start],arr[pivotIndex]

    # take care of left and right part
    i = start
    j = end
    while i<pivotIndex and j>pivotIndex:
        while arr[i]<pivot:
            i+=1
        while arr[j]>pivot:
            j-=1
        if i<pivotIndex and j>pivotIndex:
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
            j-=1
    return pivotIndex
'''
def partition(arr,start,end):
    cnt = start-1
    pivot = end
    for i in range(start,end):
        if arr[i]<arr[pivot]:
            cnt+=1
            arr[i],arr[cnt] = arr[cnt],arr[i]
    cnt+=1
    arr[pivot],arr[cnt] = arr[cnt],arr[pivot]
    return cnt
'''
def quickSort(arr,start,end):
    '''Use of quick sort algorithm'''
    # base case
    if start >= end:
        return arr
    # processing
    # partition
    p = partition(arr,start,end)
    # left part sorting
    quickSort(arr,start,p-1)
    # right part sorting
    quickSort(arr,p+1,end)

    return arr
arr = [8,5,1,7,3]
print(quickSort(arr,0,len(arr)-1))
