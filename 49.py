# FILE IO


fp = open("tut49.txt","w")

fp.write("Hi ")

fp.close()


fr = open("tut49.txt","r")

file = fr.read()

print(file)

fr.close()

#no need to close
with open("tut9b.txt","wt") as fdd: #By default r or wb
    fdd.writelines("POP")