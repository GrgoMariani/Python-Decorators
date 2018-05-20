from for_each_elem import for_each_elem
""" Shorter:
        Let's say you have a list that always contains the same items. When changing all the items in the list
            it makes sense to make a decorator that accesses all items for you and passes all the results as a list. 

    Short:
        @for_each_elem(list) decorates a function and takes a list as an argument. Then it takes each item of the list
            and passes it as an argument to the decorated function.
"""
numbers_till_twelve = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


@for_each_elem(numbers_till_twelve)
def square(elem):
    return elem*elem


@for_each_elem(numbers_till_twelve)
def cube(elem):
    return elem**3


@for_each_elem(numbers_till_twelve)
def root(elem):
    from math import sqrt
    return round(sqrt(elem), 2)


print("Numbers till twelve are {}".format(numbers_till_twelve))
print("Their squares are       {}".format(square()))
print("Their cubes are         {}".format(cube()))
print("Their roots are         {}".format(root()))
