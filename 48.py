a = 5

def func():
    global a

    a = a * 2

    print("Inside function ", a)



func()
print(f"Outside function {a}")