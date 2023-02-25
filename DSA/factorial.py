# n = int(input("enter number:"))
n =  999

counter = 1
fact = 1

while(counter <= n):
    fact = fact * counter
    counter = counter + 1

print(fact)

def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
# print(factorial(9))