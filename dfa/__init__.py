__all__ = ["set_state_and_transitions", "input_command", "print_current_state", "execute_current_state"]


dfa_states = dict()
dfa_transitions = dict()

current_state = 'START'


def set_state_and_transitions(name: str, transitions: dict):
    def wrapper(func):
        if name in dfa_states:
            print("State '{}' already taken | overwriting".format(name))
        dfa_states[name] = func
        for from_state in transitions:
            if from_state not in dfa_transitions:
                dfa_transitions[from_state] = dict()
            if transitions[from_state] in dfa_transitions[from_state]:
                print("Input '{}' already taken | overwriting".format(transitions[from_state]))
            dfa_transitions[from_state][transitions[from_state]] = name
        return func
    return wrapper


def execute_current_state():
    dfa_states[current_state]()


def input_command(input_cmd: str):
    global current_state
    if input_cmd not in dfa_transitions[current_state]:
        print("No such input '{}' from state '{}' | State not changed".format(input_cmd, current_state))
    else:
        current_state = dfa_transitions[current_state][input_cmd]


def print_current_state():
    print("Current state is '{}'".format(current_state))
