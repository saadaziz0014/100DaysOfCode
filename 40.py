# excersice 4

# encryption
import random
lst = []


def encr(text):
    if (len(text) <= 3):
        return text[::-1]
    else:
        lst = list(text)
        temp = lst[0]
        for i in range(len(text) - 1):
            lst[i] = lst[i + 1]
        lst[len(text) - 1] = temp
        for i in range(3):
            stng = chr(random.randrange(0, 26) + 97)
            lst.insert(i, stng)
            stng = chr(random.randrange(0, 26) + 97)
            lst.append(stng)
        return lst


def decr(text):
    if (len(text) <= 3):
        return text[::-1]
    else:
        lst = list(text)
        for i in range(3):
            lst.pop()
            lst.pop(i)

        temp = lst[len(text) - 1]
        for i in range(len(lst) - 1):
            lst[i + 1] = lst[i]

        lst[0] = temp

        return lst


e = encr("harry")
d = decr(e)

print(d)
