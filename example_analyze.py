from analyze import add_to_analyze, analyze, restart_analysis, add_to_analyze_time

""" Shorter:
    How about a optimizing tool for your python project that keeps track of
    the number of times you called a specific function and the total number
    of seconds that function took to call.
    
    Short:
    @add_to_analyze decorator adds functions to a hidden dictionary object which
    tracks numbers of their calls in your application.

    @add_to_analyze_time decorator gets total number of seconds the function
    took to execute.
    
    This way you can keep track of which functions in your application should
    be optimized.

    analyze() prints out functions ordered by their call number and time took
    restart_analysis() clears the dictionary and starts analysis from the start
"""

class AClass:
    @add_to_analyze
    def __init__(self):
        pass

    @add_to_analyze
    def nothing(self):
        pass

class BClass:
    @add_to_analyze
    def __init__(self):
        pass

    @add_to_analyze
    def nothing(self):
        pass

@add_to_analyze
def some_function():
    pass

item1 = AClass()
item2 = AClass()
item1.nothing()
# Print out current number of function calls
analyze()

print("----||||----")

item3 = BClass()
item3.nothing()
item3.nothing()
item3.nothing()
item3.nothing()
# Print out current number of function calls
analyze()


print("----||||----")
restart_analysis()
some_function()
some_function()
some_function()
some_function()
some_function()
some_function()
# Print out current number of function calls
analyze()

print("----||||----")
restart_analysis()

@add_to_analyze_time
def this_function_takes_some_time():
    _ = 0
    for item in range(5000):
        for __ in range(item):
            _ = _ + 1
    

this_function_takes_some_time()
analyze()
this_function_takes_some_time()
analyze()

