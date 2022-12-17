for j in range(10):
    if(j % 2 == 0):
        continue
    elif(j == 5):
        print("Loop is break")
        break
    else:
        print("number = ", j)



# do while

while True:
    a = int(input("Enter a number: "))
    if(a < 0):
        break
    else:
        print(a)