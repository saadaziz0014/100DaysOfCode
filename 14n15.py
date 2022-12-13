# Day 14 on if-elif-else

# Day 15 excercise on if

# Excercise - 2

import time

current = time.strftime('%H')
current = int(current)


if (current < 12):
  print("Good Morning")

elif (current >= 12 and current < 4):
  print("Good Afternoon")

else:
  print("Hi Sir")
