from set_arguments import set_arguments, set_function

""" Shorter:
    Do you want to always call your function with some specific arguments,
    or maybe call another function instead using the same arguments.
         (very useful while testing)
    
    Short:
    @set_arguments(*args, **kwargs) discards the arguments someone might pass
    to decorated function and sets given arguments as the only arguments
    
    @set_function(function) calls another function instead of this one
    
"""

def add_function_1(x, y):
    print("Add function 1")
    result = x+y
    print('{} + {} = {}'.format(x, y, result) )


@set_arguments(2, 3)
def add_function_2(x, y):
    print("Add function 2")
    result = x+y
    print('{} + {} = {}'.format(x, y, result) )

def multiply(x, y):
    print("Multiply")
    result = x*y
    print('{} * {} = {}'.format(x, y, result) )

@set_function(multiply)
def add_function_3(x, y):
    print("Add function 3")
    result = x+y
    print('{} + {} = {}'.format(x, y, result) )


add_function_1(10, 11)
add_function_2(10, 11)
add_function_3(10, 11)

add_function_1(1, 21)
add_function_2(1, 21)
add_function_3(1, 21)

add_function_1(6, 1)
add_function_2(6, 1)
add_function_3(6, 1)
