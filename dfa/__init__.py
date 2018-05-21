__all__ = ["set_state_and_transitions", "input_command", "print_current_state", "execute_current_state", "show_available_inputs"]


dfa_states = dict()
dfa_transitions = dict()

current_state = 'START'


def set_state_and_transitions(name: str, transitions: dict):
    name = name.upper()

    def wrapper(func):
        if name in dfa_states:
            print("State '{}' already taken | overwriting".format(name))
        dfa_states[name] = func
        dfa_transitions[name] = dict()
        for command in transitions:
            command = command.upper()
            dfa_transitions[name][command] = transitions[command].upper()
        return func
    return wrapper


def execute_current_state():
    if current_state not in dfa_states:
        print("State '{}' execution not defined".format(current_state))
        return
    dfa_states[current_state]()


def input_command(input_cmd: str):
    global current_state
    if input_cmd not in dfa_transitions[current_state]:
        print("No such input '{}' from state '{}' | State not changed".format(input_cmd, current_state))
    else:
        current_state = dfa_transitions[current_state][input_cmd]


def print_current_state():
    print("Current state is '{}'".format(current_state))


def show_available_inputs():
    if current_state in dfa_transitions:
        for cmd in dfa_transitions[current_state]:
            print("Input '{}' takes you to state '{}'".format(cmd, dfa_transitions[current_state][cmd]))
