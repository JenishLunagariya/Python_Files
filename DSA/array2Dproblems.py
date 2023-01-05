def largestrowsum(arr,row,col):
    maxx = -1
    rowIndex = -1
    for r in range(row):
        ans = 0
        for c in range(col):
            ans+=arr[r][c]
        if ans>maxx:
            maxx = ans
            rowIndex = r
    return rowIndex
# arr = [[1,2,3],[4,5,6],[7,8,9]]
# print(largestrowsum(arr,3,3))

def wavepattern(arr,row,col):
    c = 0
    while(c<col):
        if c%2==0: # down wave
            r = 0
            while(r<row):
                print(arr[r][c],end=' ')
                r+=1
        else:
            r = row-1
            while r>=0:
                print(arr[r][c],end=" ")
                r-=1
        c+=1
    return
# arr = [[1,2,3],[4,5,6],[7,8,9]]
# wavepattern(arr,3,3)

def spiralmatrix(arr,row,col):
    count = 0
    total = row*col
    # index
    startingRow = 0
    startingCol = 0
    endingRow = row-1
    endingCol = col-1
    while count <total:
        # starting row
        c = startingCol
        while c<=endingCol and count<total:
            print(arr[startingRow][c],end=" ")
            count+=1
            c+=1
        startingRow+=1
        # ending col
        r=startingRow
        while r<=endingRow and count<total:
            print(arr[r][endingCol], end = " ")
            count+=1
            r+=1
        endingCol-=1
        # ending row
        c = endingCol
        while c>=startingCol and count<total:
            print(arr[endingRow][c],end=" ")
            count+=1
            c-=1
        endingRow-=1
        # starting col
        r = endingRow
        while r>=startingRow and count<total:
            print(arr[r][startingCol],end=" ")
            count+=1
            r-=1
        startingCol+=1
    return
# arr = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
# arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# spiralmatrix(arr,3,4)

def rotate90matrix(arr,row,col):
    # row,col = col,row
    ans = [[0 for j in range(col)] for i in range(row)]
    
    for r in range(row):
        for c in range(col):
            nr = c
            nc = col-1-r
            ans[nr][nc] = arr[r][c]
    return ans
# arr = [[1,2,3],[4,5,6],[7,8,9]]
# arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# print(rotate90matrix(arr,4,4))

def binarysearchmatrix(arr,row,col,key):
    s = 0
    e = row*col - 1
    while s<=e:
        mid = s + (e-s)//2
        r = mid//col
        c = mid%row
        element = arr[r][c]
        if element == key:
            return (mid//col,mid%row)
        elif element<key:
            s = mid+1
        else:
            e = mid-1
    return -1
# arr = [[1,2,3],
#        [4,5,6],
#        [7,8,9],
#        [10,11,12]]
# print(binarysearchmatrix(arr,4,3,11))

def searchmatrix(arr,row,col,key):
    rowIndex = 0
    colIndex = col-1
    while rowIndex<row and colIndex>=0:
        element = arr[rowIndex][colIndex]
        if element == key:
            return (rowIndex,colIndex)
        elif element <key:
            rowIndex+=1
        else:
            colIndex-=1
    return -1
arr = [[1,4,7,11,15],
       [2,5,8,12,19],
       [3,6,9,16,22],
       [10,13,14,17,24]]
print(searchmatrix(arr,4,5,20))