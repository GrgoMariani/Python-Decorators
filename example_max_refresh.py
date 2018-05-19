from max_refresh import max_refresh
# Comment examples you need to see/hide
# Python >=3.3, for <3.3 check __init__.py

""" Shorter:
        Let's say you've got a method that you really shouldn't use too frequently.
        But you do.
        And now you want to fix that
    
    Short:
        @max_refresh serves as a simple read-update (observer) design pattern on
            a function it decorates. It takes (string)key and (double)timeout as
            arguments.
    
        Should the function be called again before the timeout has passed
        it doesn't call the function itself but rather returns the last value
        the function returned.

        The 'key' maps the return values and last function call times to the dictionary.
        
        Also feel free to try all the example functions without the decorator
"""
""" -------------------------------FIRST EXAMPLE-------------------------------------------- """


@max_refresh("uniquehash1", 1)
def first():
    print("This should be printed every 1 second")


@max_refresh("uniquehash2", 3)
def second():
    print("This should be printed every 3 seconds")


# Each function will be executed at most once until timeout is reached
while True:
    first()
    second()
"""  -------------------------------SECOND EXAMPLE-------------------------------------------- """


@max_refresh("uniquehash3", 2)
def increment_every_two_seconds(integer):
    return integer+1


# Decorator remembers old return value
a = 0
while True:
    a = increment_every_two_seconds(a)
    print(a)
"""  -------------------------------THIRD EXAMPLE---------------------------------------------- """


@max_refresh("uniquehash4", 1)
def increment1(integer):
    return integer+1


@max_refresh("uniquehash5", 3)
def returnAsArray(integer):
    return [integer]


# Decorator also remembers return values of any type of multiple functions
b = 0
while True:
    b = increment1(b)
    print("{} {}".format(b, returnAsArray(b)))

