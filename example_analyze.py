from analyze import analyze_number_of_calls, analyze_time_of_execution, print_analysis, restart_analysis

""" Shorter:
        How about a optimizing tool for your python project that keeps track of
        the number of times you called a specific function and the total time the
        function took.
    
    Short:
        @analyze_number_of_calls decorator adds functions to a hidden dictionary 
            object which tracks numbers of their calls in your application.

        @analyze_time_of_execution decorator gets total number of seconds the function
            took to execute.
    
        This way you can keep track of which functions in your application should
        be optimized.

        print_analysis() prints out functions ordered by their call number and time took
        restart_analysis() clears the dictionary and starts analysis from the start
"""


class AClass:
    @analyze_number_of_calls
    def __init__(self):
        pass

    @analyze_number_of_calls
    def nothing(self):
        pass


class BClass:
    @analyze_number_of_calls
    def __init__(self):
        pass

    @analyze_number_of_calls
    def nothing(self):
        pass


@analyze_number_of_calls
def some_function():
    pass


item1 = AClass()
item2 = AClass()
item1.nothing()
# PRINT IT
print_analysis()

print("-----------------------|||||||||||||||----------------------------------")

item3 = BClass()
item3.nothing()
item3.nothing()
item3.nothing()
item3.nothing()
# PRINT IT
print_analysis()


print("-----------------------|||||||||||||||----------------------------------")
restart_analysis()
some_function()
some_function()
some_function()
some_function()
some_function()
some_function()
# PRINT IT
print_analysis()

print("-----------------------|||||||||||||||----------------------------------")
restart_analysis()


@analyze_time_of_execution
def this_function_takes_some_time():
    _ = 0
    for item in range(5000):
        for __ in range(item):
            _ = _ + 1
    

this_function_takes_some_time()
print_analysis()
this_function_takes_some_time()
print_analysis()

