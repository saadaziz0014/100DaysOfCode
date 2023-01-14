import saadFunctions
import sys

p = int(input("Enter prime number p: "))
if(not saadFunctions.primeNumber(p)):
    print("Not a Prime")
    sys.exit()

q = int(input("Enter Prime Number q: "))
if(not saadFunctions.primeNumber(q)):
    print("Not a Prime")
    sys.exit()


n = p * q

totient = (p - 1) * (q - 1)

e = saadFunctions.createE(p,q,totient)
print(e)
d = saadFunctions.inverse(e,totient)

m = int(input("Message: "))
enc = (m ** e) % n
print(enc)
dec = (enc ** d) % n
print(dec)