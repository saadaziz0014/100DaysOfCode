# Day 16
# Match Case

x = 5
match x:
  case 1:
    print("One ")
  case 3:
    print("Three ")
  case _ if x < 10:
    print("Default 10")
  case _ if x >= 10:
    print("Default > 10")

