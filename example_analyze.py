from analyze import add_to_analyze, analyze, restart_analysis

""" Short:
    @add_to_analyze decorator adds functions to a hidden dictionary object which
    tracks numbers of their calls in your application.
    
    This way you can keep track of which functions in your application should
    be optimized.

    analyze() prints out the current function calls
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

