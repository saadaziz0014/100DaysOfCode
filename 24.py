# Tupples

a = (4, 8, 7, 9, 8)

b = (1)  # simple int
c = (1,)  # now tupple

# a.sort()  not in tupple
print(a)
# a.reverse() not in tupple
# print(a)
# a.sort(reverse=True) not in tupple
# print(a)
c = a.count(8)
print(c)

# not allowed in tupple
# m = a
# m[0] = 0
# print(a)
# tupples are immutable

# tupples can't be changed
# m = a.copy()
# m[0] = 7
# print(a)

# tupples are not allowed to change
# a.extend(m)
# print(a)
m = (1, 2, 3)
d = a + m
print(d)
