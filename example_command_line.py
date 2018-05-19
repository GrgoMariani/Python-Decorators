from command_line import register_command, execute_command

""" Shorter:
        A extremely fun programming pattern for simulating command line in under 50 lines of code.
        Similar to something you might see in flask. Feel free to play around.
            ---> beware, this is not how real command line works at all.

    Short:
        @register_command(string) decorator adds the function to a list of available commands.
            The function must not have any arguments. (or all arguments must have default values)

        execute_command(string) executes the function() which was registered with the given string
"""

a = 0


@register_command('print')
def function1():
    print('This message was printed because you entered print')


@register_command('increment_a')
def function2():
    global a
    a = a+1
    print(' The value of a is {}'.format(a))


@register_command('exit')
def function3():
    print("Bye Bye")
    exit(1)


if __name__ == '__main__':
    while True:
        command = input('\nInput your next command: ')
        execute_command(command)

