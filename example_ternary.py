from ternary import ternary, ternary_call

""" Shorter:
        There is an operator in C/C++ called ternary.
            (checkSomething) ? do_this_if_something_was_true : do_this_if_it_was_false
        in Python it goes like this 'do_this if something_true else do_something_else'

    Short:
        @ternary_call(func_when_result_true, func_when_result_false) automatically calls the function
            in the decorator argument based on the decorated function return result.
        @ternary(return_value_when_true, return_value_when_false) automatically returns the given 
            decorator argument based on the decorated function return result.
            
        !Important make sure decorated function returns a BOOLEAN
"""

result_true = 12
result_false = -5


def func_true():
    print("Result was True")


def func_false():
    print("Result was False")


@ternary_call(func_true, func_false)
def some_function(result: bool):
    return result


@ternary(result_true, result_false)
def some_other_function(result: bool):
    return result


some_function(True)
some_function(True)
some_function(False)

print("\n\n\n")

print(some_other_function(True))
print(some_other_function(False))
print(some_other_function(False))
