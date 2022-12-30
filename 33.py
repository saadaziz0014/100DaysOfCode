# Dictionary

dict = {
    15: "Saad",
    18: "Aziz",
    19: "Sheikh"
}

print(dict.keys())
print(dict.values())

print(dict.get(25)) # does not
# print(dict[25]) # throw error

for key in dict.keys():
    print(f"key is {key} and value is {dict[key]}")



for key, value in dict.items():
    print(f"{key}:{value}")