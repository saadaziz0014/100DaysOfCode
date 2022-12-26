# Doc String

def cube(a):
    '''Print Cube of Number'''
    return a * a * a


print(cube.__doc__)
print(cube(5))

# Simple comment


def cube2(a):
    n = 4
    '''Print Cube of Number'''
    return a * a * a


print(cube2.__doc__)
print(cube2(5))
