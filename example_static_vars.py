from static_vars import static_vars

""" Shorter:
        Static variables inside functions can be really useful

    Short:
        @static_vars(**kwargs)(func) Set keys to be used as variables inside the function namespace
            and values as the default values
"""


@static_vars(i=0, show_first_message=True)
def increase_i():
    if increase_i.show_first_message:
        print("I need to print this message first")
        increase_i.show_first_message = False
    print(increase_i.i)
    increase_i.i += 1


increase_i()
increase_i()
increase_i()
