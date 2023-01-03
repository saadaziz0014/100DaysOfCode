# try except finally

def cube1():
    try:
        inp = int(input("Enter number: "))
        print(inp ** 3)
        return 1
    except Exception as e:
        print(e)
        return 0
    print("If I am in finally I will print :(")


def cube2():
    try:
        inp = int(input("Enter number: "))
        print(inp ** 3)
        return 1
    except Exception as e:
        print(e)
        return 0
    finally:
        print("I am in finally, yuhu  :)")


cube1()
cube2()