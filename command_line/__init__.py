__all__ = ["register_command", "execute_command"]


commands = dict()


def register_command(command: str):
    def wrapper2(func):
        if command in commands:
            print("Command '{}' already taken | Overwriting".format(command))
            commands[command] = func
        else:
            commands[command] = func
        return func
    return wrapper2


def execute_command(command: str):
    if command in commands:
        commands[command]()
    else:
        print('Unknown command')
