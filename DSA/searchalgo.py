import numpy as np
# from time import time
from datetime import datetime
from collections import Counter

# start = time()
def searchLinear(arr, key) -> bool:
    for i in arr:
        if i==key:
            return 1
    return 0
arr = np.array([1,3,5,7,9,10,-1])

# print(searchLinear(arr,-1))
# end = time()
# print(f"start:{start}, end:{end}, end-start = {(end-start)*1000}")

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

# start = datetime.now()
arr = [3,5,9,13,27,30]
print(searchBinary(arr,13))
# end = datetime.now()
# print(end-start)

def swaparrayelements(arr):
    n = len(arr)
    mid = n//2
    for i in range(mid):
        arr[i], arr[-i-1] = arr[-i-1], arr[i]
    return arr

# print(swaparrayelements(arr))

def swapalternatearrayelements(arr) -> int:
    n = len(arr)
    for i in range(0,n-1,2):
        arr[i],arr[i+1] = arr[i+1],arr[i]
    return arr

# arr = np.array([1,2,3,4,5])
# print(swapalternatearrayelements(arr))
# print(arr)

def findunique(arr):
    n = len(arr)
    ans = 0
    for i in range(n):
        ans = ans^arr[i] 
    return ans

# start = time()
# arr = np.array([1,2,3,6,5])
# print(findunique(arr))
# # end = time()
# print(f"time:{end-start}")

def uniqueoccurance(arr) -> bool:  # for only positive int arrays
    n = len(arr)
    N = np.zeros(999)
    for i in range(n):
        pos = arr[i]
        N[pos]+=1
    N = N[N!=0].astype(int)
    
    Ns = np.zeros(999)
    for i in range(len(N)):
        Ns[N[i]]+=1
        if Ns[N[i]] > 1:
            return False
    return True
# start = time()
# arr = np.array([1,1,2,1,2,3])
# print(uniqueoccurance(arr))
# end = time()
# print(f"time:{end-start}")

def uniqueOccurance(arr) -> bool:  # for any interger arrays
    return len(Counter(arr).keys()) == len(set(Counter(arr).values()))
# print(uniqueOccurance(arr))

def findDuplicate(arr): # arr is of len N and have elements from 1 to N-1, with one repeating element
    ans = 0
    for i in range(len(arr)):
        ans = ans^arr[i]
    for i in range(1,len(arr)):
        ans = ans^i
    return ans

# arr = [1,2,3,4,5,2]
# print(findDuplicate(arr))

def findCommoninTwoArrays(arr1,arr2):
    ans = []
    i,j = 0,0
    N,M = len(arr1),len(arr2)
    while(i<N and j<M):
        if(arr1[i]<arr2[j]):
            i+=1
        elif(arr1[i]==arr2[j]):
            ans.append(arr1[i])
            j+=1
            i+=1
        elif arr1[i]>arr2[j]:
            j+=1
    
    if len(ans)>0:
        return ans
    return -1
# start = datetime.now()
# arr1 = [1,2,2,2,3,4]
# arr2 = [2,2,3,3]
# arr1 = [3,4,5]
# arr2 = [1,4,5]
# end = datetime.now()
# print(findCommoninTwoArrays(arr1,arr2))
# print(end-start)

def pairSum(arr,S):
    ans = []
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j] == S:
                ans.append([min(arr[i],arr[j]),max(arr[i],arr[j])])
    return sorted(ans)

# S = 5
# arr = [1,2,3,4,5]
# S = 0
# arr = [-2,-3,3,3,2]
# print(pairSum(arr,S))

def sortOne(arr):
    i = 0
    j = len(arr)-1
    while(i<j):
        while arr[i]==0:
            i+=1
        while arr[j]==1:
            j-=1
        if (i<j): # for arr[i] == 1 and arr[j]==0, swap values
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
            j-=1
    return arr

# arr = [1,1,0,0,0,1,0,0]
# print(sortOne(arr))