# facto = lambda n: 1 if n==1 else n*facto(n-1)
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
# print(factorial(5))

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(5))

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    first = 0
    second = 1
    for i in range(2,n):
        temp = second
        second = first + second
        first = temp
    ans = first + second
    return ans
# print(fib(8))

def countDistictwaysToclimbStairs(n):
    '''you need to climb n stairs, either climb 1 stair at a time or 2 stairs.
    count how many ways are there to climb n stairs'''
    if n<0:
        return 0
    elif n==0:
        return 1
    else:
        return countDistictwaysToclimbStairs(n-1)+countDistictwaysToclimbStairs(n-2)
# print(countDistictwaysToclimbStairs(5))

def isSortedArr(arr,n):
    '''check array is sorted or not'''
    # base case
    if n-2<0:
        return True
    # processing
    ans = isSortedArr(arr[:n-1],n-1)
    # recursion
    return ans and (arr[n-1] >= arr[n-2])
# arr = [1,2,3,4,6,6]
# print(isSortedArr(arr,6))

def sumArr(arr,n):
    '''give sum of array'''
    # base case
    if n==0:
        return 0
    # processing
    # recursion
    return arr[0] + sumArr(arr[1:],n-1)
# arr = [1,2,3,4,5,6]
# print(sumArr(arr,6))

def linearSearch(arr,n,key):
    '''check element present or not'''
    print("arr:",arr)
    if n==0:
        return False
    if arr[0]==key:
        return True
    else:
        return linearSearch(arr[1:],n-1,key)
# arr=[3,5,2,8,10,7]
# print(linearSearch(arr,6,0))

def binarySearch(arr,key,start,end):
    '''return index of element if present, else -1''' 
    # base case
    if start>end:
        return -1
    # processing
    mid = start + (end-start)//2
    if arr[mid]==key:
        return mid
    elif arr[mid]>key:
        end = mid-1
    else:
        start = mid+1
    # recursion
    return binarySearch(arr,key,start,end)
    
# arr = [2,3,5,7,8,10]
# print(binarySearch(arr,10,0,5))

def firstAndlastIndex(arr,key,start,end):
    '''return first and last index of repeating key in
    sorted array'''
    # base case
    if start>end:
        return (-1,-1)
    # processing
    mid = start + (end-start)//2
    if arr[mid]==key:
        firstindex = mid
        lastindex = mid

        while(arr[firstindex]==key) and firstindex-1>=0:
            firstindex -=1
        # if arr[0]!=key:
        #     firstindex+=1
        
        while (arr[lastindex]==key) and lastindex+1<=len(arr)-1:
            lastindex+=1
        # if arr[-1] != key:
        #     lastindex-=1
        return (firstindex,lastindex)
    elif arr[mid]>key:
        return firstAndlastIndex(arr,key,start,mid-1)
    else:
        return firstAndlastIndex(arr,key,mid+1,end)
# arr = [0,0,1,1,2,2,2,2]
# print(firstAndlastIndex(arr,2,0,len(arr)-1))

def peakIndexmountainArray(arr,start,end):
    '''find index of peak in mountain array'''
    # base case
    if start>end:
        return start
    # processing
    mid = start + (end-start)//2
    if arr[mid]>arr[mid+1]:
        return peakIndexmountainArray(arr,start,mid-1)
    else:
        return peakIndexmountainArray(arr,mid+1,end)
# arr = [3,4,5,1,2]
# print(peakIndexmountainArray(arr,0,len(arr)-1))

def pivotArrayindex(arr,leftsum,rightsum,index):
    '''return index where sum of all right elements and 
    sum of all left elements is same, else return -1'''
    # base case
    if index==len(arr):
        return -1
    # processing

    if rightsum==leftsum:
        return index
    else:
        index+=1
        rightsum = rightsum - arr[index]
        leftsum = leftsum + arr[index-1]
        return pivotArrayindex(arr,leftsum,rightsum,index)
# arr = [1,7,3,6,5,6]
# print(pivotArrayindex(arr,0,sum(arr[1:]),0))
# print(sum(arr))

def pivotArrayelement(arr,start,end):
    '''get pivot array element'''
    # base case
    if start>=end:
        return start
    # processing
    mid = start + (end-start)//2
    if arr[mid]>arr[0]:
        start = mid+1
    else:
        end = mid
    return pivotArrayelement(arr,start,end)
# arr = [7,9,1,2,3]
# print(pivotArrayelement(arr,0,len(arr)-1))

from math import fabs
from sys import float_info
def SqrtD(val,prev):
    next = (prev+val/prev)/2
    if fabs(next-prev) < float_info.epsilon*(next):
        return next
    else:
        return SqrtD(val,next)
# print(SqrtD(36,1))

def bookAllowcation(arr,m):
    """Book Allocation Problem which use Binary search 
    pattern"""
    pass

def painterPartition(arr,m):
    """Painter's Partition Problem: 
    Use of Binary search pattern"""
    pass

def aggressiveCows(arr,m):
    """Aggresive Cows Problem: 
    Use of Binary search pattern"""
    pass

def reverseString(string,ans):
    '''return reversed string'''
    # base case
    if len(string) == 0:
        return ans
    ans = ans + string[-1]
    return reverseString(string[:-1],ans)
# string = "hello"
# print(reverseString(string,""))

def reverseArr(arr,start,end):
    '''reverse array'''
    # base case
    if start > end:
        return arr
    arr[start],arr[end] = arr[end],arr[start]
    return reverseArr(arr,start+1,end-1)
# arr = ["h","e","l","l","o","o"]
# print(reverseArr(arr,0,len(arr)-1))

def checkPalindrome(string,start,end):
    '''check for string is palindrome or not'''
    # base case
    if start>end:
        return True
    # processing
    if string[start] == string[end]:
        return checkPalindrome(string,start+1,end-1)
    else:
        return False
# string = "olanlo"
# print(checkPalindrome(string,0,len(string)-1))

def aPowerb(a,b):
    '''return a**b'''
    '''if b == 0:
        return 1
    else:
        return a * aPowerb(a,b-1)'''
    # base case
    if b==0:
        return 1
    elif b==1:
        return a
    # recursion
    ans = aPowerb(a,b//2)
    # processing
    if b%2 == 0:
        return ans*ans
    else:
        return a*ans*ans
# a,b = 2,5
# print(aPowerb(a,b))

def bubbleSort(arr,n):
    '''Use of Bubble sort algorithm: shift bigger one to right side'''
    # base case
    if n==0 or n==1:
        return arr
    # processing
    for i in range(0,n-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
    # recursion
    return bubbleSort(arr,n-1)
# arr = [2,5,1,6,9,3]
# print(bubbleSort(arr,6))

def sortSelection(arr,start,n):
    '''Use of Selection sort algorithm: shift smaller one to left side'''
    # base case
    if start== n-1:
        return arr
    for i in range(start+1,n):
        if arr[i] < arr[start]:
            arr[i],arr[start] = arr[start],arr[i]
    # recursion
    return sortSelection(arr,start+1,n)
# arr = [29,72,98,13,87,66,52,51,36]
# print(sortSelection(arr,0,len(arr)))

def sortInsertion(arr,n,start):
    '''Use of Insertion sort algorithm:'''
    # base case
    if start == n:
        return arr
    # processing
    temp = arr[start]
    j = start - 1
    while j>=0:
        if arr[j]>temp:
            arr[j+1] = arr[j]
        else:
            break
        j-=1
    arr[j+1] = temp
    # recursion
    return sortInsertion(arr,n,start+1)
# arr = [29,72,98,13,87,66,52,51,36]
# arr = [2,5,1,6,9,3]
# print(sortInsertion(arr,len(arr),1))

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
# arr = [2,4,5,1,3]
# arr = [29,72,98,13,87,66,52,51,36]
# arr = [-4,5,3,2,-1]
# print(mergeSort(arr,0,len(arr)-1))

def inversionCount():
    pass

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

# arr = [2,4,3,1,7]
# arr = [-4,5,3,2,-1]
# print(quickSort(arr,0,len(arr)-1))

def solve(arr,output,index,ans):
    # base case
    if index >= len(arr):
        ans = ans.append(output)
        return
    # exclude element from output
    solve(arr,output,index+1,ans)
    # include element to output
    output = output + [arr[index]]
    solve(arr,output,index+1,ans)

def subArr(arr):
    '''return all sub arr of an Array'''
    ans = []
    output = []
    index = 0
    solve(arr,output,index,ans)
    return ans
# arr = [1,2,3,4]
# print(subArr(arr))

def solution(string,output,index,ans):
    if index>=len(string):
        if len(output) != 0:
            ans = ans.append(output)
        return
    # exclude
    solution(string,output,index+1,ans)
    # include
    output = output + string[index]
    solution(string,output,index+1,ans)

def subSequence(string):
    '''return subsequence of string'''
    ans = []
    output = ""
    index = 0
    solution(string,output,index,ans)
    return ans
# string = "abc"
# print(subSequence(string))

def rotateArray(arr,m,start,n):
    # base case
    if start>=m:
        return arr
    # shift by 1 rotation
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[-1] = temp
    return rotateArray(arr,m,start+1,n)
# arr = [1,2,3,4,5]
# print(rotateArray(arr,4,0,5))

def phoneKeypadCombinations(string,index,ans,output,dic):
    """return all possible combinations of two keys between 2-9
    ex: 2->abs and 3->def; combinations:[ad,ae,af,bd,be,bf,cd,ce,cf]"""
    if len(string) == 0:
        return ans
    # base case
    if index >= len(string):
        ans  = ans.append(output)
        return
    # processing
    value = dic[string[index]]
    for i in range(len(value)):
        output+=value[i]
        phoneKeypadCombinations(string,index+1,ans,output)
        output = output[:-1]
    return ans

'''def phoneKeypadCombinations(string,index,ans,output):
    # base case
    if index >= len(keys):
        ans = ans.append(output)
        return ans
    # processing
    if len(output) == 0:
        first = dic[keys[index]]
        for i in range(len(first)):
            output += first[i]
            phoneKeypadCombinations(string,index+1,ans,output)
            output = ""
    else:
        second = dic[keys[index]]
        for i in range(len(second)):
            output+=second[i]
            phoneKeypadCombinations(string,index+1,ans,output)
            output = output[0]
    return ans'''
# dic = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
# keys = "27"
# ans = []
# output = ""
# print(phoneKeypadCombinations(keys,0,ans,output))
def swapPositions(lis, pos1, pos2):
     
    lis[pos1], lis[pos2] = lis[pos2], lis[pos1]
    return lis

from math import factorial
def permutationArray(arr,ans,index):
    '''return all possible permutations of arr'''
    '''ex: [1,2,3]->[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]'''
    # base case:
    if index>=len(arr):
        ans = ans.append(arr)
        return
    # processing
    for i in range(len(arr)):
        print(i)
        arr = swapPositions(arr,index,i)
        permutationArray(arr.copy(),ans,index+1)
        #backtrack to original array
        arr = swapPositions(arr,index,i)
        if len(ans) >= factorial(len(arr)):
            break
    return ans
# arr = [1,2,3]
# ans = []
# print(permutationArray(arr,ans,0))

def isSafe(x,y,n,visited,m):
    if (x>=0 and x<n) and (y>=0 and y<n) and (visited[x][y]==0 and m[x][y]==1):
        return True
    else:
        return False

def findPath(m,n,ans,x,y,visited,path):
    # base case
    if x == n-1 and y == n-1:
        ans = ans.append(path)
        return
    visited[x][y] = 1
    # 4 movement - down,up,right,left
    # Down
    newx = x+1
    newy = y
    if isSafe(newx,newy,n,visited,m):
        path+="D"
        findPath(m,n,ans,newx,newy,visited,path)
        path = path[:-1] # backtrack
    # Left
    newx = x
    newy = y-1
    if isSafe(newx,newy,n,visited,m):
        path+="L"
        findPath(m,n,ans,newx,newy,visited,path)
        path = path[:-1] # backtrack
    # Right
    newx = x
    newy = y+1
    if isSafe(newx,newy,n,visited,m):
        path+="R"
        findPath(m,n,ans,newx,newy,visited,path)
        path = path[:-1] # backtrack
    # Up
    newx = x-1
    newy = y
    if isSafe(newx,newy,n,visited,m):
        path+="U"
        findPath(m,n,ans,newx,newy,visited,path)
        path = path[:-1] # backtrack
    visited[x][y] = 0 # backtrack
    return 

def ratInmaze(m,n):
    '''return all posible path in maze from src to destination for rat'''
    ans = []
    if m[0][0] == 0:
        return ans
    srcx = 0
    srcy = 0
    visited = [[0 for i in range(n)] for i in range(n)]
    path = ""
    findPath(m,n,ans,srcx,srcy,visited,path)
    ans = sorted(ans)
    return ans
m = [[1,0,0,0],
     [1,1,0,1],
     [1,1,0,0],
     [0,1,1,1]]
n = 4
print(ratInmaze(m,n))