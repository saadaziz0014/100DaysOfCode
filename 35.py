# else with loops
# else execute when loop end not break

for i in range(5):
    print(i)
else:
    print("i khtm")


for i in range(5):
    if (i % 2 != 0):
        print("Odd Present", i)
        break

else:
    print("Nhi mila")



inp = int(input("Num: "))
while inp >= 0:
    print("Drust ", inp)
    inp-=1
else:
    print("Khtm km ha zero sy" ,inp)