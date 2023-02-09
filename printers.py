import time, sys
from colors import *

special_char = {}


def print_human(machine):
    """
    Print the current machine as a human-readable format, then exits
    """
    sorted_dict = dict(sorted(machine.items()))
    for key in sorted_dict.keys():
        for elem in sorted_dict.get(key):
            print("{}  {}  {}  {}".format(key, elem[0], elem[1], elem[2]))


def print_machine(name, machine):
    """
    Print the current machine as a python dictionary, to make it possible
    for the user to add it to this python script, in the block line 27 and below.
    User needs to add it to the machines dictionary after that, to be able to call it
    :param name: the name of the dictionary
    """
    print("### COPY THIS IN THE BLOCK LINE 27 ###")
    print(name + " = {")
    for key in machine.keys():
        print("\t{}: {},".format(key, machine.get(key)))
    print("}")
    print("######################################")


def print_state(current_band, current_index, current_state, action):
    """
    Print the current band, index, state, action (for debugging purpose)
    :param action: the last action (it's not a global)
    """
    print("Band : {}\nIndex : {}\nState : {}\nLast Action : {}".format(current_band, current_index, current_state,
                                                                       action))


def modify_letter(letter):
    if letter in special_char:
        return "" + special_char[letter] + letter + bcolors.ENDC
    return letter


def print_band(iterator, current_band, current_index, display_inline, display_sleep, etat=None):
    """
    Print the current band, with green current index
    """
    my_str = "[" + str(iterator) + "] "
    for i in range(0, len(current_band)):
        if i == current_index:
            my_str += bcolors.OKGREEN + current_band[i] + bcolors.ENDC  # don't forget ENDC !
        else:
            my_str += modify_letter(current_band[i])
    if etat is not None:
        my_str += " -- " + str(etat)
    if display_inline:
        print("\r{}   ".format(my_str), end="", flush=True)
    else:
        print(my_str)
    time.sleep(display_sleep)


def error(string):
    """
    Print a red string
    :param string: the string to print
    """
    print(bcolors.FAIL + string + bcolors.ENDC)
    sys.exit(1)
