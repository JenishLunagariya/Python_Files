def reversearray(arr): # Reverse an array
    n = len(arr)-1
    for i in range(n//2 +1 ):
        arr[i],arr[n-i] = arr[n-i],arr[i]
    return arr
# arr = [1,2,3,4,5,11,16]
# print(reversearray(arr))

def reverseafterMindexarray(arr,m): # start reversing array from index m
    s = m+1
    e = len(arr)-1
    while(s<=e):
        arr[s],arr[e] = arr[e],arr[s]
        s+=1
        e-=1
    return arr
# arr = [1,2,3,4,5,11,16]
# print(reverseafterMindexarray(arr,2))

def mergesortedarray(arr1,arr2): #create sorted array by merging two sorted arrays
    i=0
    j=0
    arr=[]
    while(i<len(arr1) and j<len(arr2)):
        if arr1[i]<=arr2[j]:
            arr.append(arr1[i])
            i+=1
        else:
            arr.append(arr2[j])
            j+=1
    while(i<len(arr1)):
        arr.append(arr1[i])
        i+=1
    while(j<len(arr2)):
        arr.append(arr2[j])
        j+=1
    return arr
# arr1 = [1,3,5,7,9,10,12]
# arr2 = [2,4,6,7,8]
# print(mergesortedarray(arr1,arr2))

# arr1 has len of m+n and arr2 has len of n, only first m elements from arr1 to be 
# merged with arr2. later n elements of arr1 are 0s, which should be replaced when 
# merging of two arrays occurs.
def mergesortedarraysintofirstarray(arr1,arr2):
    i=0
    j=0
    while(i<len(arr1) or j<len(arr2)):
        if arr1[i] != 0:
            if arr1[i]<=arr2[j]:
                i+=1
            else:
                arr1.insert(i,arr2[j])
                j+=1
                arr1.pop(-1)
        else:
            arr1.insert(i,arr2[j])
            arr1.pop(-1)
            i+=1
            j+=1
    return arr1
# arr1 = [1,2,3,0,0,0]
# arr2 = [2,5,6]
# print(mergesortedarraysintofirstarray(arr1,arr2))

def moveszeros(arr): # just shift all the zeros to right without sorting arr
    nonzeroval=0
    for j in range(len(arr)):
        if arr[j]!=0:
            arr[j],arr[nonzeroval] = arr[nonzeroval],arr[j]
            nonzeroval+=1
    return arr
# arr = [2,0,-1,3,0,0,1]
# print(moveszeros(arr))

def rotatearray(arr,m):
    for i in range(m):
        arr.insert(len(arr),arr[0])
        arr.pop(0)
    return arr
# arr = [1,2,3,4,5,6]
# print(rotatearray(arr,2))

def sortedandrotated(arr):
    pair = 0
    for i in range(len(arr)):
        if arr[i-1]>arr[i]:
            pair+=1
            if pair>1:
                return False
    return True
# arr = [3,3,3]
# print(sortedandrotated(arr))

def sumofarray(arr1,arr2): # takes array as single int and return sum in form of arr
    i=len(arr1)-1
    j=len(arr2)-1
    carry = 0
    ans = []
    while i>=0 and j>=0:
        val1 = arr1[i]
        val2 = arr2[j]
        sum = val1 + val2 + carry
        carry = sum//10
        sum = sum%10
        ans.insert(0,sum)
        i-=1
        j-=1
    while i>=0:
        sum = arr1[i] + carry
        carry = sum//10
        sum = sum%10
        ans.insert(0,sum)
        i-=1
    while j>=0:
        sum = arr2[j] + carry
        carry = sum//10
        sum = sum%10
        ans.insert(0,sum)
        j-=1
    while carry!=0:
        sum = carry
        carry = sum//10
        sum = sum%10
        ans.insert(0,sum)
    return ans
# arr1 = [1,2,3]
# arr2 = [9,9]
# print(sumofarray(arr1,arr2))


from heapq import heappop, heappush
def Kthsmallestelement(arr,k): # -> kth smallest ele; ex: 3rd smallest ele.
    maxheap = []
    for i in range(k):
        heappush(maxheap,-arr[i])
    for i in range(k,len(arr)):
        if arr[i] < -maxheap[0]:
            heappop(maxheap)
            heappush(maxheap,-arr[i])
    return -maxheap[0]
# arr = [7,10,4,3,20,15]
# k = 3
# print(Kthsmallestelement(arr,k))

def Kthhighestelement(arr,k):
    minheap = []
    for i in range(k):
        heappush(minheap,arr[i])
    for i in range(k,len(arr)):
        if arr[i] > minheap[0]:
            heappop(minheap)
            heappush(minheap,arr[i])
    return minheap[0]
# arr = [7,10,4,3,20,15]
# k = 6
# print(Kthhighestelement(arr,k))

def sortArrof012(arr,n):
    zeroval = 0
    for i in range(n):
        if arr[i]==0:
            arr[i],arr[zeroval] = arr[zeroval],arr[i]
            zeroval+=1
    oneval = zeroval
    for i in range(oneval,n):
        if arr[i] == 1:
            arr[i],arr[oneval] = arr[oneval],arr[i]
            oneval+=1
    return arr
# arr = [0,2,1,2,0,1,2]
# print(sortArrof012(arr,len(arr)))

def movenegative(arr,n):
    '''move all negative to left'''
    negativeIndex = 0
    for i in range(n):
        if arr[i]<0:
            arr[i],arr[negativeIndex] = arr[negativeIndex],arr[i]
            negativeIndex+=1
    return arr
# arr = [1,0,4,-1,-3]
# print(movenegative(arr,len(arr)))

def unionOftwoArr(a1,a2):
    '''return union arr of both arrays'''
    return len(set(a1+a2))
# a1 = [1,3,5,4,2,6]
# a2 = [1,4,2]
# print(unionOftwoArr(a1,a2))

def intersectionofTwoArr(a1,a2):
    '''return intersaction of two arrays'''
    ans = []
    for i in set(a1):
        if i in set(a2):
            ans.append(i)
    return ans
# a1 = [1,3,5,4,2,6]
# a2 = [1,4,2,8]
# print(intersectionofTwoArr(a1,a2))

def MaxContiguousSubarrSum(arr):
    '''return maximum sum of contiguous subarray'''
    '''maxsize=-9223372036854775807'''
    from sys import maxsize
    max_sofar = -maxsize
    max_ending_here = 0
    for i in range(len(arr)):
        max_ending_here = max_ending_here + arr[i]
        if max_ending_here < -maxsize:
            max_ending_here = -maxsize
        if max_ending_here > max_sofar:
            max_sofar  = max_ending_here
    return max_sofar