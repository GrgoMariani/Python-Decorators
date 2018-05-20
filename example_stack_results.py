from stack_results import stack_results, pop_result


@stack_results
def function1(number: int):
    return number


@stack_results
def function2(text: str):
    return text


if __name__ == "__main__":
    function1(2)
    function2('Some text')
    function1(3)
    function1(7)
    function2('Some other text')
    print(pop_result())
    print(pop_result())
    print(pop_result())
    print(pop_result())
    print(pop_result())
    print(pop_result())
    print(pop_result())
