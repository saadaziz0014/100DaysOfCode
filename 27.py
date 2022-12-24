# Excercise 3
listSaad = ["Capital of Australia? ", "Canbera", 20, "Biggest City of Pakistan? ",
            "Karachi", 25, "T20 WC final teams? ", "Pakistan and England", 45]


sum = 0

length = len(listSaad)

for i in range(0, length, 3):
    ans = input(listSaad[i])
    if (ans == listSaad[i + 1]):
        sum = sum + listSaad[i + 2]
    else:
        print("Sorry Incorrect for answer number", int(i/3) + 1)
        break

print("Finished")
print("Amount =", sum, "$")
