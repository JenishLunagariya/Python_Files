n = int(input("enter number:"))

counter = 1
fact = 1

while(counter <= n):
    fact = fact * counter
    counter = counter + 1

print(fact)