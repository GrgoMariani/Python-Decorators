from TODO import TODO

""" Shorter:
        Function not yet done? Use this decorator then to print it out.

    Short:
        @TODO(func)
            replace your function call with a function that prints out that it is still being developed

"""


@TODO
def function_1():
    print("function 1")


@TODO
def function_2():
    print("function 2")


@TODO
def function_3(x, y):
    print("function 3 {]".format(x+y))


def function_4():
    print("function 4")


function_1()
function_2()
function_3(3, 2)
function_4()
