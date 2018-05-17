from set_arguments import set_arguments

""" Shorter:
    Do you want to always call your function with some specific arguments.
         (very useful while testing)
    
    Short:
    @set_arguments(*args, **kwargs) discards the arguments someone might pass
    to decorated function and sets given arguments as the only arguments
    
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


add_function_1(10, 11)
add_function_2(10, 11)

add_function_1(1, 21)
add_function_2(1, 21)

add_function_1(6, 1)
add_function_2(6, 1)
