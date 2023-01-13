fp = open("mySaad.txt", "w")

fp.write("Hioaaa")
fp.writelines("\nH\ne\nl\nl\no\n")
fp.close()

fr = open("mySaad.txt", "r")
print(fr.read())
fr.seek(0)
str = fr.read(3) # less than 3
fr.seek(0)
print(fr.readline(4))
print(str)
fr.close()

fcsv = open("newCsv.csv", "w+")

fcsv.writelines("5,6,3")
listT = []
fcsv.seek(0)
while True:
    num = fcsv.read(1)
    if(num == ''):
        break
    if(num != ','):
        listT.append(int(num))

fcsv.close()

sum = 0
for i in listT:
    sum = sum + i

print(sum)