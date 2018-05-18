from print_me import print_me

""" Shorter:
        Print Print Print
            (very useful while testing)
    
    Short:
        @print_me prints inputs and outputs of the decorated function
"""


@print_me
def add(x, y):
    return x+y


@print_me
def multiply_by_two(x):
    return add(x, x)


@print_me
def nothing():
    pass


add(2, 3)
multiply_by_two(5)
nothing()
