# f-String

# old method
a = "I am {name} and {degree} student"
b = "Range is {1} and docs{0}"
c = "Percentage is {per:.2f}"
print(a.format(name="Saad", degree="bsse"))
print(b.format("tree", 2.33333))
print(c.format(per=2.655448))

# new above 3.6

name = input("Enter Your Name: ")
passion = input("Enter passion: ")

print(f"My Name is {name} and want to be {passion} developer")

# print as it is

print(f"Name is {{name}}")