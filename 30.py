# recursion


# num = int(input("Enter Number: "))
# factorial
def factorial(n):
    if(n == 0 or n == 1):
        return 1
    
    return n * factorial(n - 1)

print(factorial(5))

# febonacci

def feb(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return feb(n - 2) + feb(n - 1)


listB = []

for i in range(10):
    listB.append(feb(i))

for i in range(10):
    print(listB[i])

