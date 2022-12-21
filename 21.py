def nameF(fn="muhammad", mn="saad", ln="aziz"):
    return fn + mn + ln


n = nameF()
print(n)

n = nameF("ahmad")
print(n)


# Functions argumets

n = nameF(mn="hadi")
print(n)


def avg(a, b=4):
    return (a+b)/2


c = avg(4)
print(c)


def sum(*num):
    sum = 0
    for i in num:
        sum = sum + i

    print("Sum = ", sum)


sum(4)
sum(4, 4, 8)
sum(4, 2, 3, 6, 4, 5)
sum(4, 1, 1)
sum(4, 4, 7, 8)


def dictP(**dictdata):
    print("Name = ", dictdata["name"], " and Age = ", dictdata["age"])


dictP(name="Saad", age=22)
