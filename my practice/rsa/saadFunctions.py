def primeNumber(num):
    check = 0
    if (num == 1):
        return True
    elif (num <= 0):
        return False
    else:
        for i in range(2, num):
            if (num % i == 0):
                check = 1
                return False

        if (check == 0):
            return True


def inverse(num, modN):
    ans = 0
    i = 1
    while i < 26:
        if (((modN * i) + 1) % num == 0):
            ans = ((modN * i) + 1) // num
            return ans
        i += 1

    return 0


def createE(p, q, totient):
    for i in range(2, totient):
        if (i != p and i != q and primeNumber(i)):
            return i
