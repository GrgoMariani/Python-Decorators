from dfa import set_state_and_transitions, input_command, print_current_state, execute_current_state
""" Deterministic Finite Automaton Emulator
    Shorter:
        Nothing too fancy. Just a simple DFA emulator. Set state name and transitions to that state
        in the decorator arguments.
    
    Short:
        @set_state_and_transitions takes arguments string and dict as state name and transitions.
        
        print_current_state() prints the state the automaton is currently in.
        
        execute_current_state() executes the current function associated with the state
        
        input_command() inputs the given string to the automaton 
        
    Example:
        This example shows the next automaton:
            START   [1<-->1]   A  [1<-->0]  B
              [0<-------------------------->0]
"""


@set_state_and_transitions('START', {'A': '1', 'B': '0'})
def function1():
    print('You have to start somewhere')


@set_state_and_transitions('A', {'START': '1', 'B': '1'})
def function2():
    print('Here')


@set_state_and_transitions('B', {'START': '0', 'A': '0'})
def function3():
    print('There')


if __name__ == "__main__":
    print_current_state()
    execute_current_state()
    while True:
        inString = input('\nWhat is your next input: ')
        input_command(inString)
        print_current_state()
        execute_current_state()




