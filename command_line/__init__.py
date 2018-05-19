__all__ = ["register_command", "execute_command"]

commands = dict()


def register_command(command: str):
    def wrapper(func):
        if command in commands:
            print("Command '{}' already taken | Overwriting".format(command))
            commands[command] = func
        else:
            commands[command] = func
        return func
    return wrapper


def execute_command(command: str):
    if command == "":
        return None
    if command in commands:
        commands[command]()
    else:
        print("Unknown command. Type '--help' for options")


@register_command('--help')
def help():
    for command in commands:
        print("'{}' calls {}()".format(command, commands[command].__name__))
