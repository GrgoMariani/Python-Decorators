from dfa import set_state_and_transitions, input_command, print_current_state, execute_current_state, show_available_inputs
""" Deterministic Finite Automaton Emulator
    Shorter:
        Nothing too fancy. Just a simple DFA emulator. Set state name and transitions to that state
            in the decorator arguments.
    
    Short:
        @set_state_and_transitions takes arguments string and dict as state name and transitions.
        
        print_current_state() prints the state the automaton is currently in.
        
        execute_current_state() executes the current function associated with the state
        
        input_command() inputs the given string to the automaton
        
        show_available_inputs() prints all possible inputs from the current state and the states those inputs
            lead to.
        
    Example:
        This example shows the next automaton:
            START   [0--> <--1]   A  [0--> <--1]  B
             [ 1-->                           <--0 ]
"""


@set_state_and_transitions('start', {'0': 'A', '1': 'B'})
def function1():
    print('You have to start somewhere')


@set_state_and_transitions('A', {'0': 'B', '1': 'START'})
def function2():
    print('Here')


@set_state_and_transitions('B', {'0': 'START', '1': 'A'})
def function3():
    print('There')


if __name__ == "__main__":
    print_current_state()
    execute_current_state()
    show_available_inputs()
    while True:
        command = input('\nWhat is your next input: ')
        if command:
            input_command(command)
            execute_current_state()
        else:
            print_current_state()
            show_available_inputs()




