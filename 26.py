# Excercise 2

import time


name = input("Enter Name: ")
current = time.strftime('%H')
current = int(current)


if (current < 12):
    print("Good Morning ", name)

elif (current >= 12 or current < 4):
    print("Good Afternoon ", name)

else:
    print("Hi ", name)
