def searchBinary(arr,key): # input sorted array
    n = len(arr)
    start = 0
    end = n-1
    
    while start <= end:
        mid = start + (end-start)//2  # (start+end)//2
        if arr[mid] == key:
            return mid  # return index if present
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return -1  # return -1 if not present

def firstlastindex(arr,key): # return first and last index of 
    n = len(arr)
    start = 0
    end = n-1
    while start <= end:
        mid = start + (end-start)//2  # (start+end)//2
        if arr[mid] == key:
            first = mid
            last = mid

            while arr[first] == key and first-1 >=0:
                first = first - 1
            if arr[0] != key:
                first+=1

            while arr[last] == key and last+1 <= (n-1):
                last = last + 1
            if arr[-1] != key:
                last-=1
            
            return first, last
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return -1,-1 # return (-1,-1) if not present

# arr = [2,2,2,2,0,0,1,1]
# arr = [0,0,1,1,2,2,2,2]
# arr = [0,0,1,1,1,1,2,2]
# arr = [0,0,1,2,2,3,3,3]
# print(firstlastindex(arr,2))

def peakindexMountainarray(arr):
    s = 0
    e = len(arr) - 1
    while(s<e):
        mid = s + (e-s)//2
        if arr[mid]<arr[mid+1]:
            s = mid+1
        else:
            e = mid
    return s

# arr = [3,4,5,1]
# print(peakindexMountainarray(arr))

def Pivotarrayindex(arr): # if left elements' sum and right elements' sum of pivot same,return index of pivot
    initial = 0
    n = len(arr)
    l = 0
    r = 0
    while(initial+1<n):
        r = r + arr[initial+1]
        initial+=1
    pointer=0
    while(pointer<n):
        if l == r:
            return pointer
        pointer+=1
        l = l + arr[pointer-1]
        r = r - arr[pointer]
    return -1
# arr = [1,7,3,6,5,6]
# print(Pivotarrayindex(arr))

def PivotarrayElement(arr):
    s = 0
    e = len(arr)-1
    while(s<e):
        mid = s + (e-s)//2
        if arr[mid]>=arr[0]:
            s = mid +1
        else:
            e = mid
    return s

arr = [7,9,1,2,3]
print(PivotarrayElement(arr))

def getPosition(arr,key): # search element in pivot rotated sorted array
    pivot = PivotarrayElement(arr)
    n = len(arr)
    if key>=arr[pivot] and key<=arr[n-1]:
        return searchBinary(arr[pivot:],key=key) + pivot
    else:
        return searchBinary(arr[0:pivot],key)

# arr = [7,8,1,3,5]
# print(getPosition(arr,3))

def sqrtint(value): #input is square of integer 
    s = 0
    e = value
    ans = -1
    # get intger
    while(s<=e):
        m = s + (e-s)//2
        if m*m == value:
            return m
        elif m*m > value:
            e = m-1
        else:
            ans = m
            s = m+1
    # get decimal places
    while((ans+0.1)**2 < value):
        ans+=0.1
    while((ans+0.01)**2 < value):
        ans+=0.01
    return round(ans,2)
# print(sqrtint(50))

"""Book Allocation Problem which use Binary search pattern"""
def isBookPossible(arr,m,mid):
    studentCount = 1
    pageSum = 0
    for i in range(len(arr)):
        if(pageSum+arr[i]<=mid):
            pageSum+=arr[i]
        else:
            studentCount+=1
            if studentCount>m or arr[i]>mid:
                return False
            pageSum = arr[i]
    return True

def bookallocation(arr,m):
    s = 0
    Sum = sum(arr)
    e = Sum
    ans = -1
    while s<=e:
        mid = s + (e-s)//2
        if isBookPossible(arr,m,mid):
            ans = mid
            e = mid-1
        else:
            s = mid + 1
    return ans

# arr = [10,20,30,40]
# arr = [12,34,67,90]
# arr = [5,17,100,11]
# print(bookallocation(arr,2))

"""Painter's Partition Problem: use of Binary search pattern"""
def isPainterPossible(arr,m,mid):
    NumberOfPainters = 1
    PaintersPartitions = 0
    for i in range(len(arr)):
        if (PaintersPartitions + arr[i]) <= mid:
            PaintersPartitions+=arr[i]
        else:
            NumberOfPainters+=1
            if (NumberOfPainters>m or arr[i]>mid):
                return False
            PaintersPartitions=arr[i]
    return True

def painterpartition(arr,m): # m defined no. of painters for partition
    s = 0
    e = sum(arr)
    ans = -1
    while(s<=e):
        mid = s + (e-s)//2
        if isPainterPossible(arr,m,mid):
            ans = mid
            e = mid - 1 
        else:
            s = mid + 1
    return ans

# arr = [5,5,5,5]
# print(painterpartition(arr,2))

"""Aggresive Cows Problem: use of Binary search pattern"""
def isCowPossible(arr,m,mid):
    CowCounter = 1
    lastPos = arr[0]
    for i in range(len(arr)):
        if arr[i]-lastPos >=mid:
            CowCounter+=1
            if CowCounter == m:
                return True
            lastPos = arr[i]
    return False

def aggresivecows(arr,m):
    arr = sorted(arr)
    s = 0
    e = max(arr)
    ans = -1
    while s<=e:
        mid = s + (e-s)//2
        if isCowPossible(arr,m,mid):
            ans = mid
            s = mid+1
        else:
            e = mid-1
    return ans

# arr = [4,1,2,3,6]
# print(aggresivecows(arr,3))