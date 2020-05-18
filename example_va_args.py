from va_args import va_args, va_args2

""" Shorter:
        Check how va_args macro in C works.

    Short:
        @va_args(func) The function func now uses a string as a first argument and a va_args as others
        
        @va_args2(n)(func) The function uses a string as a (n+1)-th argument.

"""


@va_args
def printf(string):
    print(string)


printf("There are %d lights", 4)
printf("%d divided by %f is %s", 11, 3.5, "pi")


@va_args2(2)
def logger_printf(log_lvl, num_spaces, string):
    if log_lvl >= 4:
        for i in range(0, num_spaces):
            print(" ", end="")
        print(string)


logger_printf(0, 8, "Won't print the numbers %d %d %d", 4, 5, 7)
logger_printf(4, 8, "Will print %d %d %d", 10, 11, 13)
