def isprime(n):
    for i in range(2,n):
        if n%i==0:
            return 0
    return 1

# Seive of Eratosthenes
def countprime(n):
    prime = [True]*n
    cnt = 0
    prime[0] = prime[1] = False
    for i in range(2,n):
        if prime[i]:
            cnt+=1
            for j in range(2*i,n,i):
                prime[j] = False
    return cnt
# print(countprime(5000000))

# simple seive --> print all the prime till limit
def simplesieve(n):
    prime = [True]*n
    prime[0] = prime[1] = False
    for i in range(2,n):
        if prime[i]:
            for j in range(2*i,n,i):
                prime[j] = False
    for i in range(len(prime)):
        if prime[i]:
            print(i,end=" ")
    return
# n = 23
# simplesieve(n)

# Segmented seive
def segmentedsieve(n):
    pass
# n = 23
# segmentedsieve(n)

# GCD
def hcm(a,b):
    if a==0:
        return b
    elif b==0:
        return a
    while a!=b:
        if a>b:
            a = a-b
        elif a<b:
            b = b-a
    return a
# print(hcm(8,12))

# LCM
def lcm(a,b):
    gcd = hcm(a,b)
    return (a*b)//gcd
# print(lcm(8,12))

# modular expontiation --> (x^n)%m
def modexpontiation(x,n,m):
    res = 1
    while n>0:
        if n&1: # for odd n
            res = (res%m) * (res%m)
        x = ((x%m)*(x%m))%m
        n = n>>1 # get the division for divided by 2
    return res
# print(modexpontiation(3,1,2))
print(modexpontiation(4,3,10))
