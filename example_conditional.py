from conditional import conditional

""" Shorter:
        A different approach on condition pattern, it can also be easily implemented with ternary decorator

    Short:
        @conditional(func_that_needs_to_be_checked) executes the decorated function only if the result of the
            func_that_needs_to_be_checked is True

        !Important make sure that decorator argument is a function and returns a BOOLEAN
"""

some_parameter = True


def isParameterTrue():
    global some_parameter
    return some_parameter


@conditional(isParameterTrue)
def do_something():
    print("I did something")


print("\n STEP 1 ")
do_something()
print("\n STEP 2 ")
some_parameter = False
do_something()
print("\n STEP 3 ")
some_parameter = True
do_something()


# #####################################################
# # But how about this ################################
# #####################################################
def isNowDay():
    import datetime
    hour = datetime.datetime.now().hour
    if 8 <= hour <= 20:
        return True
    return False


@conditional(isNowDay)
def do_only_if_day():
    print("This will be only shown if it's daytime")


print("\n Last Example")
do_only_if_day()