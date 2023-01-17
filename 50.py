# read or read line
# write or writeline

with open('tut50.txt',"w") as f:
    f.writelines("I am boy\nI live in Lahore\nI am developer\n")

i = 0
with open("tut50.txt","r") as fr:
    while True:
        line = fr.readline()
        if not line:
            break
        print(f"Line number {i} is line: {line}")
        i+=1