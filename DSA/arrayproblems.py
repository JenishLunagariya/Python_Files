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

def getMinDiff(arr,k):
    '''arr consist of positive numbers, we can either increase or decrease each element by k.
    return minimum difference betweeen max. and min. element of array after operation'''
    mid = sum(arr)//len(arr)
    low = mid - k
    high = mid + k
    for i in range(len(arr)):
        if arr[i] <= low:
            arr[i] = arr[i] + k
        elif arr[i] >= high:
            arr[i] = arr[i] - k
        else:
            if arr[i] < mid:
                arr[i] = arr[i] + k
            else:
                arr[i] = arr[i] -k
    ans = max(arr) - min(arr)
    return ans
# arr = [3,9,12,16,20]
# k = 3
# print(getMinDiff(arr,k))

def minJumps(arr,index,counter):
    '''arr consists of elements, starts from first element, move steps as per value in element'''
    # base case
    if index >= len(arr)-1:
        return counter
    elif arr[index] == 0:
        return -1
    counter+=1
    index = index + arr[index]
    return minJumps(arr,index,counter)
# arr = [1,3,5,8,9,2,6,7,6,8,9]
# arr = [1,4,3,2,6,7]
# print(minJumps(arr,0,0))

def merge2SortedArr(arr1,arr2,m,n):
    '''merge two sorted arays without using extra space'''
    for i in range(n-1,-1,-1):
        last = arr1[m-1]
        j = m-2
        while (j>=0 and arr1[j]>arr2[i]):
            arr1[j+1] = arr1[j]
            j-=1
        if last>arr2[i]:
            arr1[j+1] = arr2[i]
            arr2[i] = last
# arr1 = [1,5,9,10,15,20]
# arr2 = [2,3,8,13]
# merge2SortedArr(arr1,arr2,6,4)
# print("arr1:",arr1,"arr2:",arr2)

def mergeIntervals(arr):
    '''merge those subarrays into one subarrays which are overlaping, else leave as it is'''
    i=0
    while i < len(arr):
        n = len(arr)
        if i<n-1:
            subarr = arr[i]
            nextsubarr = arr[i+1]
            if subarr[1] >= nextsubarr[0] and i<n-1:
                # merge subarr into one
                newarr = [subarr[0],nextsubarr[1]]
                del arr[i:i+2]
                arr.insert(i,newarr)
                continue
        i+=1
    return arr
# arr = [[1,3],[2,6],[8,10],[15,18]]
# arr = [[1,4],[4,5]]
# arr = [[0,2],[2,5],[5,8],[10,13],[13,18]]
# print(mergeIntervals(arr))

def PermutationOfArr(arr,index,ans):
    '''returns all permutations of arr as arr
    ex: [1,2,3] => [[1,2,3],[1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1]]'''
    # base case
    if index >= len(arr):
        ans = ans.append(arr)
        return
    for i in range(index,len(arr)):
        arr[i],arr[index] = arr[index],arr[i]
        PermutationOfArr(arr.copy(),index+1,ans)
        arr[i],arr[index] = arr[index],arr[i]
    return ans
# arr = [1,2,3]
# ans = []
# print(PermutationOfArr(arr,0,ans))

def CountInversion(arr,n):
    '''O(n^2)'''
    # output = 2; ans = (2,1),(4,1),(4,3)
    ctr = 0 
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] > arr[j]:
                ctr +=1
    return ctr
# arr = [2,4,1,3,5]
# arr = [2,3,4,5,6]
# arr = [3,5,1,10,9,2,6,8] 
# n = 8
# print(CountInversion(arr,n))

def merge(arr,start,end,mid):
    invCount = 0
    temp = [0 for i in range(end-start+1)]
    index1 = start
    index2 = mid
    tempIndex = 0
    while index1<mid and index2<=end:
        if arr[index1] <= arr[index2]:
            temp[tempIndex] = arr[index1]
            index1+=1
        else:
            temp[tempIndex] = arr[index2]
            invCount += mid-index1
            index2+=1
        tempIndex+=1
    while index1<mid:
        temp[tempIndex] = arr[index1]
        index1+=1
        tempIndex+=1
    while index2<=end:
        temp[tempIndex] = arr[index2]
        index2+=1
        tempIndex+=1
    k=0
    for x in range(start,end):
        arr[x] = temp[k]
        k+=1
    return invCount

def mergeSort(arr,start,end):
    invCount = 0
    if end>start:
        mid = start+(end-start)//2
        invCount = mergeSort(arr,start,mid)
        invCount+=mergeSort(arr,mid+1,end)
        invCount+=merge(arr,start,end,mid+1)
    return invCount

def getInversions(arr):
    '''O(nlogn) using mergesort algorithm'''
    return mergeSort(arr,0,len(arr)-1)
# arr = [2,4,1,3,5] # 3
# arr = [3,5,1,10,9,2,6,8] # 11
# arr = [8, 4, 2, 1] # 6
# arr = [1, 20, 6, 4, 5] # 5
# print(getInversions(arr))

def maxProfit(prices):
    index = 0
    buy = index
    sell = index+1
    profit = prices[sell]-prices[buy]
    while sell<len(prices):
        if prices[sell]-prices[buy]<0:
            buy +=1
        else:
            sell+=1
        if sell<len(prices):
            if prices[sell]-prices[buy] > profit:
                profit = prices[sell]-prices[buy]
        # index+=1
    return profit
# arr = [7,1,5,3,6,4] #5
# arr = [3,4,1,6] #5
# arr = [7,6,4,3,1] #0
# print(maxProfit(arr))

def getPairsCounts(arr,ksum):
    '''find all pairs whose sum equals ksum'''
    m = [0]*10000
    n = len(arr)
    for i in range(n):
        m[arr[i]] += 1
    twice_count = 0
    for i in range(n):
        twice_count+=m[sum-arr[i]]
        if sum-arr[i] == arr[i]:
            twice_count-=1
    return int(twice_count/2)
# arr = [1,5,7,1]
# sum = 6
# arr = [1, 5, 7, 1, 5]
# sum = 6
# arr = [10, 12, 10, 15, 1, 7, 6, 5, 4, 2, 1, 1, 1]
# sum = 11
# arr = [1,1,1,1]
# sum=2
# print(getPairsCounts(arr,sum))

def CommonElement(arr1,arr2,arr3):
    '''find common element in three sorted array'''
    map = dict()
    n1 = len(arr1)
    n2 = len(arr2)
    n3 = len(arr3)
    for i in range(n1):
        map[arr1[i]] =1
    for j in range(n2):
        if arr2[j] in map.keys():
            map[arr2[j]] +=1
        else:
            map[arr2[j]] = 1
    for k in range(n3):
        if arr3[k] in map.keys():
            map[arr3[k]] +=1
        else:
            map[arr3[k]] = 1
    ans = []
    for key,value in map.items():
        if value >=3:
            ans.append(key)
    return ans
# arr1 = [1, 5, 10, 20, 40, 80]
# arr2 = [6, 7, 20, 80, 100]
# arr3 = [3, 4, 15, 20, 30, 70, 80, 120]
# print(CommonElement(arr1,arr2,arr3))

def Rearrange(arr):
    '''arr consists of negative and positive int, rearrange it so that negative and positive int
    comes in alternate order, while mainataining original order of arr'''
    first = 0
    second = 1
    n = len(arr)
    while first < n:
        if first%2 == 0: #even => negative val places
            if arr[first] >=0:
                # traverse second to find negative num
                while arr[second] >=0:
                    if second < n-1:
                        second+=1
                    else:
                        break
                if arr[second]<0:
                    val = arr[second]
                    del arr[second]
                    arr.insert(first,val)
                
            else:
                first+=1
                second = first+1
        else: #odd => positive val places
            if arr[first] <0:
                # traverse second to find positive num
                while arr[second] < 0:
                    if second < n-1:
                        second+=1
                    else:
                        break
                if arr[second] >=0:
                    val = arr[second]
                    del arr[second]
                    arr.insert(first,val)
            else:
                first+=1
                second = first+1
        if second == n-1:
            break
    return arr

# arr = [1, 2, 3, -4, -1, 4,-5]  #[-4, 1, -1, 2, -5, 3, 4]
# arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8,-2]  #[-5, 5, -2, 2, -8, 4, -2, 7, 1, 8, 0]
# print(Rearrange(arr))

def subArrayExists(arr):
    '''check whether there is a subarray present with 0-sum or not'''
    n = len(arr)
    curr = 0
    dic = {}
    for i in range(n):
        curr += arr[i]
        if curr in dic or curr == 0:
            return True
        dic[curr] = 1
    return False
# arr = [4,2,-4,1,1]
# arr = [4,2,0,1,6]
# print(subArrayExists(arr))

def maxProduct(arr,n):
    '''find maximum product subarray'''
    ans = float('-inf')
    Sum = 1
    for i in range(n):
        Sum*=arr[i]
        ans = max(ans,Sum)
        if Sum ==0:
            Sum = 1
    Sum = 1
    for i in range(n-1,-1,-1):
        Sum*=arr[i]
        ans = max(ans,Sum)
        if Sum == 0:
            Sum = 1
    return ans
arr = [6,-3,-10,0,2]
# arr = [0,0,-5,0,0]
# arr  =[2, 3, 4, 5, -1, 0]
print(maxProduct(arr,5))

def findLongestConseqSubseq(arr):
    '''find len of subsequence such that, elements in subsequence are consecutive integers'''
    n = len(arr)
    # TODO: complete this.

arr = [2,6,1,9,4,5,3]
arr = [1,9,3,10,4,20,2]