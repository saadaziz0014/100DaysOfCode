a = [4,8,7,9,8]

a.sort()
print(a)
a.reverse()
print(a)
a.sort(reverse=True)
print(a)
c = a.count(8)
print(c)

# Original change
m = a 
m[0] = 0
print(a)
# not good practice

m = a.copy()
m[0] = 7
print(a)

a.extend(m)
print(a)

d = a + m
print(d)