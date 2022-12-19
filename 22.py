a = [1,2,1,"Saad",True,45.36]

print(a[1:4:2])

a = [i for i in range(25) if i % 2 > 0]

print(a)

print(a[:2])

if 2 in a:
    print("Yes")
else:
    print("No")

# Same in string
if "aa" in "saad":
    print("Yes")
else:
    print("No")
