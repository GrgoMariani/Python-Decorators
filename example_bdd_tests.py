from bdd_tests import register_testing_suite, set_given, set_when, set_then, given, when, then
""" Shorter:
        Recently I stumbled upon something called Behaviour Driven Development so I gave this a go.
        It's nothing special, and I believe this can be improved a lot, but I'm sure that everyone can appreciate
        the fun in coding this way.

    Short:
        register_testing_suite function sets the class instance to be called for testing.

        @set_given/when/then decorators set decorated functions to be executed
        
        given()/when()/then() executes the given functions
        
    Feel free to improve this code
"""


class Class_To_Test:
    def __init__(self):
        self.a = 0
        self.b = 0

    def set_parameters(self, a, b):
        self.a = a
        self.b = b

    def multiply(self):
        return self.a * self.b


class Testing_Suite:
    def __init__(self):
        self.class_to_test = None

    @set_given("Class constructed")
    def construct_class(self):
        self.class_to_test = Class_To_Test()

    @set_when("Parameter 'a' negative")
    def param_a_negative(self):
        self.class_to_test.set_parameters(-2, 5)

    @set_then("assert multiplication result less than zero")
    def assert_error_when_multiplying(self):
        assert self.class_to_test.multiply() < 0


if __name__ == "__main__":
    a = Testing_Suite()
    register_testing_suite(a)
    given("Class constructed")
    when("Parameter 'a' negative")
    then("Assert multiplication result less than zero")
