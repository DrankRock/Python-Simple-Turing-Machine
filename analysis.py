"""
Here i'm trying to determine if a state is infinite
My first idea is to check if a state can read everything and don't get ton any other state

MAT, BIG ISSUE. This only works with single band.

"""

from printers import *

completes = []
out_transitions = {}

def analyse(transition_list, bands):
    """
        analyse the content of the machine to detect divergence

        The input is a dictionnary of transition, such as :
        0: [['|', 'B', 1]],
        1: [['B', 'R', 0]]

        The band is also necessary, to know the complete vocabulary

        possible_values = all the possible characyers in the machine
        state_can_read = dictionnary of the characters read by each state
        complete_states = list of states that read all the characters
    """

    possible_values, state_can_read = extract_possible_values(transition_list, bands)
    # # Determine the states that read all the possible chars
    complete_states = []
    for key, value in state_can_read.items():
        if sorted(value) == sorted(possible_values):
            complete_states.append(key)
    global completes
    completes = complete_states
    out_states = {}
    global out_transitions
    out_transitions = out_states

    # # Determine the states who only go to themselves
    # # + Initialize the list containing the output of each state
    final_states = []
    for key, value in transition_list.items():
        out_states[key] = []
        for sublist in value:
            item = sublist[-1]
            if item not in out_states[key]:
                out_states[key].append(item)
        out_states[key] = sorted(out_states[key])
        if str(out_states[key][0]) == str(key) and len(out_states) == 1:
            final_states.append(key)

    # Second check : is a group of states in a cycle who all read everything and only lead to each others
    second_check = []
    for state in transition_list.keys():
        if is_state_infinite_cycle(state, []):
            second_check.append(state)
    if len(second_check) != 0:
        print(bcolors.OKVIOLET, "The analysis shows that the states {} are likely divergent, because they can read\n"
                                "every character and don't lead to any state that can't read every caracter \n"
                                "Enter q to quit, anything else to continue :".format(str(second_check)), bcolors.ENDC)
        key = input()
        if key == "q":
            exit(1)

    return possible_values, second_check # list of all values, list of infinite states


def is_state_infinite_cycle(state, seen):
    if state not in completes:
        return False
    if state in seen:
        return True
    else :
        seen.append(state)
        for next_state in out_transitions[state]:
            if not is_state_infinite_cycle(next_state, seen):
                return False
        return True



def extract_possible_values(transition_list, bands):
    """
    Extract the dictionnary of the machine, all possibles characters, and also the values that can be read by a
    state
    """
    values = []
    not_values = ['R', 'L']
    states_can_read = {}
    for band in bands:
        for car in band:
            if car not in values and car not in not_values:
                values.append(car)

    for key, my_list in transition_list.items():
        # [['|', 'R', 'B', '2'], ['B', 'N', 'B', '3']],
        states_can_read[key] = []
        for sublist in my_list:

            for elem in sublist[:-1]:  # don't check last element as it's the next step
                if elem not in states_can_read[key] and elem not in not_values:
                    states_can_read[key].append(elem)
                if elem not in values and elem not in not_values:
                    values.append(elem)
    return sorted(values), states_can_read
