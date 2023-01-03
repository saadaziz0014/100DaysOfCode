# try except


try:
    a = int(input("Num: "))
    print(a * a)
except:
    print("Enter Integer")



myList = [1,2,3,4,5]

try:
    ind = int(input("Enter Index: "))
    print(myList[ind])
except IndexError as e:
    print(e)


try:
    inp = int(input("Enter number: "))
    print(inp ** 3)
except Exception as e:
    print(e)