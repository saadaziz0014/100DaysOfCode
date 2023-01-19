# fseek and ftell

f = open("tut50.txt", "r")

f.seek(2)

print(f.read(2))

print(f.tell())