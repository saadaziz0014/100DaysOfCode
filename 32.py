myset = {1, 2, 3, 4}
myset2 = {4, 5, 6}

print(myset.union(myset2))  # does not update original

myset.update(myset2)  # now update

print(myset)

print(myset.symmetric_difference(myset2))  # not common in both

print(myset.intersection(myset2))  # not update original

myset.intersection_update(myset2)

print(myset)

print(myset.difference(myset2))

myset.add(5)
myset.add(7)

print(myset)

print(myset.pop())
print(myset)

del myset2  # delete the set

myset.clear()  # clear the set
