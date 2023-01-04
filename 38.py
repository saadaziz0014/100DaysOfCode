# raise an error

inp = int(input("Enter number between 4 and 8: "))

if(inp >= 4 and inp <= 8):
    print("Good")
else:
    raise ValueError("Wrong input")



val = input("Enter Quit: ")

if(val != 'Quit'):
    raise ValueError("Wrong")