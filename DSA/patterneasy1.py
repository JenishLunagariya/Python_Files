# n = int(input("enter n:"))
def numberpattern(n):
    i=1
    while(i<=n):
        j=1
        while(j<=n):
            print(j,end=" ")
            j = j+1
        print()
        i=i+1
    return

# numberpattern(4)

def reversenumberpattern(n):
    i=1
    while(i<=n):
        j=1
        while(j<=n):
            print(n-j+1,end=" ")
            j += 1
        print()
        i+=1
    return

# reversenumberpattern(4)

def continuenumberpattern(n):
    i=1
    j=1
    while(i<=n):
        while(j<= n*i):
            print(j,end=" ")
            j+=1
        i+=1
        print()
    return

# continuenumberpattern(4)

def rownumberpattern(n):
    i=1
    while(i<=n):
        j=1
        while(j<=i):
            print(i,end=" ")
            j+=1
        print()
        i+=1
    return

# rownumberpattern(4)

def trianglenumberpattern1(n):
    i=1
    counter=1
    while(i<=n):
        j=1
        while(j<=i):
            print(counter,end=" ")
            j+=1
            counter+=1
        print()
        i+=1

# trianglenumberpattern1(4)

def reversenumberpattern(n):
    i=1
    while (i<=n):
        j=1
        while(j<=i):
            print(i+1-j,end=" ")
            j+=1
        print()
        i+=1
    return
# reversenumberpattern(4)

def alphabetpattern(n):
    i = 0
    while(i<n):
        j=0
        while(j<n):
            print(chr(ord('A')+i),end=" ")
            j+=1
        i+=1
        print()
    return
# alphabetpattern(4)

def continuealphabetpattern(n):
    i = 1
    j = 1
    while (i<=n):
        while(j<=n*i):
            print(chr(ord('A')+j-1),end=' ')
            j+=1
        i+=1
        print()
    return

# continuealphabetpattern(4)

def diagonalalphabetpattern(n):
    i=1
    while(i<=n):
        j=1
        while(j<=n):
            print(chr(ord('A')+i+j-2),end=" ")
            j+=1
        i+=1
        print()
    return
# diagonalalphabetpattern(4)

def trianglealphabetpattern(n):
    i=1
    counter = 0
    while(i<=n):
        j=1
        while(j<=i):
            print(chr(ord('A')+counter),end=" ")
            counter+=1
            j+=1
        i+=1
        print()
    return
# trianglealphabetpattern(4)

def trianglediagonalalphabetpattern(n):
    i=1
    while(i<=n):
        j=1
        while(j<=i):
            print(chr(ord('A')+i+j-2),end=" ")
            j+=1
        print()
        i+=1
    return

# trianglediagonalalphabetpattern(4)

def reversetrianglealphabetpattern(n):
    i=0
    while(i<n):
        j=0
        while(j<=i):
            print(chr(ord('A')+n-i+j-1),end=" ")
            j+=1
        i+=1
        print()
    return
# reversetrianglealphabetpattern(4)

def trianglestarpattern(n):
    i=1
    while(i<=n):
        j=1
        while(j<=i):
            print("*",end=" ")
            j+=1
        i+=1
        print()
    return
# trianglestarpattern(4)

def mirrortrianglestarpattern(n):
    i=1
    while(i<=n):
        j=1
        space = n-i
        while(j<=n):
            if (j<=space):
                print(" ",end=" ")
            else:
                print("*",end=" ")
            j+=1
        i+=1
        print()
    return
# mirrortrianglestarpattern(4)

def reversemirrortrianglestarpattern(n):
    i=1
    while(i<=n):
        j=1
        space = i-1
        while(j<=n):
            if(j<=space):
                print(" ",end=" ")
            else:
                print("*",end=" ")
            j+=1
        i+=1
        print()
    return
# reversemirrortrianglestarpattern(4)

def equilateraltrianglenumberpattern(n):
    i=1
    while(i<=n):
        j=1
        while(j<=2*n-1):
            if(j<=n-i or j>=n+i):
                print(" ",end=" ")
            elif (j<=n):
                print(i+j-n, end=" ")
            elif (j>n):
                print(i+n-j,end=" ")
            j+=1
        i+=1
        print()
    return
# equilateraltrianglenumberpattern(7)

def dabangpattern(n):
    i=1
    while(i<=n):
        j=1
        while(j<=n-i+1):
            print(j,end=" ")
            j+=1
        star = (i-1)*2
        while(star):
            print("*",end=" ")
            star-=1
        j=1
        while(j<=n-i+1):
            print(n-i-j+2, end=" ")
            j+=1
        i+=1
        print()
    return
# dabangpattern(5)

def fibonacci(n):
    a=0
    b=1
    i=1
    while(i<=n):
        if (i==1):
            print(a,end=" ")
        elif i==2:
            print(b,end=" ")
        else:
            print(a+b,end=" ")
            a,b = b,a+b
        i+=1
    return
fibonacci(9)
