__all__ = ["register_testing_suite", "set_given", "set_when", "set_then", "given", "when", "then"]

givens = dict()
whens = dict()
thens = dict()

testing_suite = None


def register_testing_suite(testing_s):
    global testing_suite
    testing_suite = testing_s


def set_given(text: str):
    def wrapper(func):
        givens[text.lower()] = func
        return func
    return wrapper


def set_when(text: str):
    def wrapper(func):
        whens[text.lower()] = func
        return func
    return wrapper


def set_then(text: str):
    def wrapper(func):
        thens[text.lower()] = func
        return func
    return wrapper


def given(text: str):
    print("GIVEN: {}".format(text))
    if not text.lower() in givens:
        print("ERROR: Method '{}' not registered with given".format(text))
    else:
        givens[text.lower()](testing_suite)


def when(text: str):
    print("WHEN:  {}".format(text))
    if not text.lower() in whens:
        print("ERROR: Method '{}' not registered with when".format(text))
    else:
        whens[text.lower()](testing_suite)


def then(text: str):
    print("THEN:  {}".format(text))
    if not text.lower() in thens:
        print("ERROR: Method '{}' not registered with then".format(text))
    else:
        thens[text.lower()](testing_suite)
