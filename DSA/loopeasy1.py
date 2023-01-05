def Prime(n):
    i=2
    while(i<n):
        if(n%i==0):
            print("Not Prime")
            return
        i+=1
    print("Prime")
    return
# Prime(31)

def digitsum(n):
    sum=0
    while(n>0):
        sum += n%10
        n=int(n/10)
    print(sum)
    return
# digitsum(99)

def countonebits(n): #binary input
    count = 0
    while(n>0):
        if(n%10!=0):
            count+=1
        n = int(n/10)
    print(count)
    return
# countonebits(100000000000001000001)

def reverseint(n):
    reverse = 0
    negative = 0
    if n<0:
        negative=1
        n = -n
    
    while(n!=0):
        last = n%10
        reverse = reverse*10 + last
        n = int(n/10)

    if negative == 1:
        reverse = -reverse
    return reverse
# print(reverseint(-123))
# print(reverseint())

def inttobinary(n):
    binlist = []
    binary = 0
    while(n!=0):
        binlist.append(n%2)
        n = int(n/2)
    for i in range(len(binlist)-1,-1,-1):
        binary = binary*10 + binlist[i]
    return binary
# print(inttobinary(56))

def binarytoint(n):
    integer = 0
    i=0
    while n!=0:
        last = n%10
        n = n//10
        integer+= last*pow(2,i)
        i+=1
    return integer
# print(binarytoint(10100))

def complimentint(n):
    n = inttobinary(n)

    #convert binary to list
    l1 = []
    while(n!=0):
        l1.append(n%10)
        n = int(n/10)
    l2 = []
    for i in range(len(l1)-1,-1,-1):
        l2.append(l1[i])

    # compliment
    for i in range(len(l2)):
        if l2[i] == 0:
            l2[i] = 1
        else:
            l2[i] = 0

    # convert list to binary
    compliment = 0
    for i in l2:
        compliment = compliment*10 + i
    
    compliment = binarytoint(compliment)
    return compliment
# print(complimentint(21))

def findcompliment(n):
    powerof2s = 2
    temp = n
    while(temp>>1):
        temp>>=1
        powerof2s<<=1
        # print(powerof2s)
    return powerof2s-n-1
# print(findcompliment(21))

def approxsqrt(n): # only integer as output, decimal ignored
    i=1
    counter = 0
    while(i<=n):
        n = n-i
        counter+=1
        i+=2
    return counter
# print(approxsqrt(24))

def isPowerofTwo(n):
    for i in range(31):
        if n==pow(2,i):
            return f"2^{i} = {n}"
    
    return "Not power of 2"
# print(isPowerofTwo(1024))

def subSet(arr):
    l = []
    for i in range(2**len(arr)):
        subset = []
        for j in range(len(arr)):
            mask = 1<<j
            if i & mask != 0:
                subset.append(arr[j])
        l.append(subset)
    return l
# arr = [1,2,3]
# print(subSet(arr))

def subSequece(string):
    l = []
    for i in range(2**len(string)):
        subset=""
        for j in range(len(string)):
            mask = 1<<j
            if (i & mask != 0):
                subset+=string[j]
        if len(subset) != 0:
            l.append(subset)
    return l
# string = "abc"
# print(subSequece(string))