import sys
import argparse
import time

import printers
from colors import *
from printers import *

'''
TODO : 1:easy, 2: easy but long, 3: hard, 4: impossible at the moment
 2   - gdb mode with s, j <n steps>, c, b <state>, p 
 3   - n-bands /!\ Most important
 1   - -nd, --no-display to show only last band
 2   - save machines to .machines file with -s
        --> load 
        --> append multiple machines
        --> load machines from custom file 
 2   - Complete http://morphett.info/turing/turing.html support
        maybe -m <morphet file>
 1   - Accept transitions from file
        -t <filename>
 1   - accept * as "do not move"
 2   - .config to save parameters, maybe run -d to run default specified in config
    
 4   - Make a full blown GUI
    Many of these imply a new file "file_manager.py"

'''
number_of_bands = 1
current_band = []
current_index = 0
current_state = 0
precedent = ""
iterator = 0
end_symbols = []
display_inline = False
display_sleep = 0
special_color_char = {}
nuplets = 4
nodisplay = False
maximum_iteration = sys.maxsize
check_maximum = True

encountered_bands_states = []

#################################
# ADD YOUR CUSTOM MACHINES HERE #
cleaner = {
    0: [['|', 'B', 1]],
    1: [['B', 'R', 0]]
}

### COPY THIS IN THE BLOCK LINE 27 ###
divide3 = {
    0: [['|', 'R', 'B', '1']],
    1: [['|', 'R', 'B', '2'], ['B', 'N', 'B', '3']],
    2: [['|', 'N', 'R', '2'], ['B', 'N', '|', '3']],
    3: [['|', 'N', 'L', '3'], ['B', 'R', 'R', '4']],
    4: [['B', 'L', 'B', '8'], ['|', 'R', 'B', '5']],
    5: [['B', 'R', 'B', '7'], ['|', 'R', 'B', '6']],
    6: [['|', 'R', '|', '4'], ['B', 'R', 'B', '7']],
    7: [['B', 'N', 'B', '7']],
    8: [['|', 'N', 'B', '8']],
}
######################################

# Don't forget to add it below !
machines = {
    "cleaner": cleaner,
    "divide": divide3
}


# ## END OF CUSTOM MACHINES  ## #
#################################

def grouped(iterable, n):  # https://stackoverflow.com/a/5389547
    return zip(*[iter(iterable)] * n)


def add_encountered_state(state):
    global encountered_bands_states
    new_state = str(current_band[0]) + str(current_state) + str(state) + str(current_index)
    if new_state in encountered_bands_states:
        return False
    else:
        encountered_bands_states.append(new_state)
        return True


def extract_parenthesis(transition):
    # we have the chance that parenthesis should be next to each other
    # you can note that i compare only two parenthesis. if there is more, nyëh
    splitted_one = transition.split(") (")
    splitted_one_one = splitted_one[0].split("(")[1]
    splitted_one_two = splitted_one[1].split(")")[0]
    if len(splitted_one_two) != len(splitted_one_one):
        raise ValueError("All bands should be treated at oonce. Incorrect transition : \"{}\"".format(transition))
    dummy_transition = ""
    deepness = 0

    for i in range(len(transition)):
        current = transition[i]
        if current == "(":
            deepness += 1
        elif current == ")":
            deepness -= 1
            dummy_transition += "D"
        else :
            if deepness == 0:
                dummy_transition += current
    print("dumm : ", dummy_transition)
    return splitted_one_one, dummy_transition


def init_dict(transition):
    # initialisation phase on the first transition
    init_split = transition.split(' ')
    global number_of_bands
    if "(" in transition:
        content_of_one_parenthesis, dummy = extract_parenthesis(transition)
        number_of_bands = len(content_of_one_parenthesis)
        size_of_uplets = len(dummy.split(" "))
    else :
        size_of_uplets = len(transition[1:-1].split(" "))
    global nuplets
    nuplets = size_of_uplets



def make_machine(transitions):
    """
    create the dictionary representation of the machine from the transition in arguments
    :param transitions: a list_integ of string in the format "<start state> <read> <action> <end state>"
    """
    try:
        my_dict = {}
        init_dict(transitions[0])

        for elem in transitions:
            current = elem.split(' ')
            state = int(current[0])
            if not my_dict.get(state):
                my_dict[state] = []  # dictionary of the form : <start state>: [ [<read>, <action>, <end state>], [...]]
            elem_list = []
            for i in range(1, nuplets):
                elem_list.append(current[i])
            my_dict.get(state).append(elem_list)
        global machine
        machine = my_dict
    except Exception as ex:
        error("Exception caught during machine creation :\n{}".format(ex))


def init_band(integers, band):
    """
    Initialize the Machine's memory or "band"
    :param integers: a list_integ of integers
    :param band: a string containing a custom band
    """
    global current_band
    current_band.append(band)
    current_band[0] += "BBB"
    global current_index
    current_index += 3  # because I add BBB for clarity
    current_band[0] += add_integers(integers)
    current_band[0] += "BBB"


def add_integers(list_integ):
    """
    add the integers to the band with the format n = "||..|B"
                                                      12..n
    :param list_integ: a list of integers as strings
    :return: the newly created band
    """
    my_band = ""
    if list_integ is not None and len(list_integ) > 0:
        for item in list_integ:
            try:
                current = int(item)
                for i in range(0, current + 1):
                    my_band += "|"
                my_band += "B"
            except Exception as exp:
                error("Exception caught during integers initialization :\n{}".format(exp))
        return my_band
    else:
        return ""


def ending(i=0):
    """
    Print the ending infos and exits
    :param i: set to 1 if it was called in the transition exception screen
    """
    if display_inline:
        print("")
    if i == 2 :
        print("Reached in ∞ steps")
        print(bcolors.OKRED + "Maximum step value reached. This machine seems to diverge.")
        print("If no maximum value was set, the step 2,147,483,647 was reached.")
        print("To remove this maximum value, launch machine with '-nm, --no-maximum' parameter." + bcolors.ENDC)
        sys.exit(1)
    if nodisplay:
        print_band(iterator, current_band[0], current_index, display_inline, display_sleep, current_state)
    print("-----------------\nEnd Reached")
    for elem in end_symbols:
        try:
            print("Number of " + elem + " : " + str(current_band[0].count(elem)))
        except Exception as e:
            print("Number of " + elem + " : 0")
            print(e)
    if i == 0:
        print("Reached in ∞ steps")
    else:
        print("Reached in {} steps".format(iterator))
    if i != 0:
        print("Note : Ended because of unknown transition")
    else:
        print(bcolors.OKRED + "Note : Ended because of infinite state" + bcolors.ENDC)
    sys.exit(1)


def do_nothing():
    return 0


def next_state():
    """
    Calculates the next state, from the current state
    """
    global current_index
    global current_state
    global current_band
    global iterator
    global precedent

    current_char = current_band[0][current_index]  # character pointed by index
    possibilities = machine.get(int(current_state))  # possible transitions
    machine_step = []
    try:
        for i in range(0, len(possibilities)):
            if possibilities[i][0] == current_char:
                machine_step = possibilities[i]
    except Exception as exp:
        # no possible transition was found -> End
        ending(1)
    if not machine_step:
        ending(1)
    all_steps = machine_step[1:(nuplets - 2)]
    all_steps.reverse()

    for step in all_steps:
        if not add_encountered_state(step):
            print("state already encountered")
            ending()
        if step == 'R':  # move right
            current_index += 1
            if current_index == len(current_band[0]) - 1:
                current_band[0] += "B"
        elif step == 'L':  # move left
            current_index -= 1
            if current_index == 0:
                current_band[0] = "B" + current_band[0]
        elif step == 'N':  # do nothing
            do_nothing()
            # do nothing 
        else:  # replace by character instead of moving
            band = list(current_band[0])
            band[current_index] = step
            current_band[0] = "".join(band)  # modify the band
        iterator += 1
        if not nodisplay:
            print_band(iterator, current_band[0], current_index, display_inline, display_sleep, current_state)
    current_state = machine_step[nuplets - 2]  # update current state

    # Check if the machine is in an infinite state
    current = str(current_state) + "," + str(current_index) + "," + str(current_char)
    if current == precedent:
        ending()
    precedent = str(current_state) + "," + str(current_index) + "," + str(current_char)


# Parse arguments
parser = argparse.ArgumentParser()

# Working
parser.add_argument('-b', '--band', help="Starting band for the program",
                    default="", type=str)
parser.add_argument('-c', '--colors', help="Specify a color for a character ( -c B red ). l to list colors",
                    type=str, nargs='+')
parser.add_argument('-di', '--display-inline', help="Display the current line inline", action='store_true')
parser.add_argument('-ds', '--display-sleep', help="sleep n milliseconds between each step", default=0, type=int)
parser.add_argument('-es', '--end-symbols', help="Specify the symbols to count after ending. Format : -es Y S",
                    nargs='+', type=str, default="|")
parser.add_argument('-i', '--int', help="integers to add to the band", type=int, nargs='+')
parser.add_argument('-m', '--machine', help="Use a custom machine previously added to the source code above,"
                                            " line 27 and below", type=str)
parser.add_argument('-mi', '--maximum_iteration', help="Specify the maximum step (to detect divergence)", type=int)
parser.add_argument('-nd', '--no-display', help="Show only the initial and ending band", action='store_true')
parser.add_argument('-nm', '--no-maximum', help="Remove the default maximum step value of 2^31-1", action='store_true')
parser.add_argument('-p', '--print', help="Print a python version of the machine, to add it in the code, "
                                          "line 27 and below", type=str)
parser.add_argument('-ph', '--print-human', help="Print the current machine as a human readable format",
                    action='store_true')
parser.add_argument('-si', '--start-index', help="Starting index of the machine", type=int, default=0)
parser.add_argument('-t', '--transitions', help="Transitions (format : '<start state> <read> <action> <end state>'\n"
                                                "Example : \"0 B | 1\" \"0 | | 0\"", type=str, nargs='+')
# Not Working

args = parser.parse_args()

if args.colors:
    if args.colors[0] == "l" and len(args.colors) == 1:
        available_colors()
        sys.exit(1)
    elif args.colors:
        for char, color in grouped(args.colors, 2):
            try:
                special_color_char[char] = color_dict[color.lower()]
            except Exception:
                print(
                    "Exception caught during color creating. \nAre you sure that {} and {} are valid ?".format(char,
                                                                                                               color))
                available_colors()
                sys.exit(1)
        printers.special_char = special_color_char

if args.maximum_iteration:
    maximum_iteration = int(args.maximum_iteration)


# Initialize
if not args.machine and not args.transitions:
    error("Error : Must specify either a custom machine or a set of transitions.\n"
          "See SimpleTuring.py -h for more details.")

if not args.band and not args.int:
    error("Error : Must specify a band or integers\nSee SimpleTuring.py -h for more details.")

init_band(args.int, args.band)

if not args.transitions:
    # then custom machine
    machine = machines.get(args.machine)
    if machine is None:
        error("Error : Unknown machine \"{}\"".format(args.machine))
else:
    make_machine(args.transitions)

if args.start_index != 0:
    current_index = args.start_index

if args.print:
    printers.print_machine(args.print[0], machine)

if args.print_human:
    printers.print_human(machine)

end_symbols += args.end_symbols
display_inline = args.display_inline
display_sleep = args.display_sleep / 1000
nodisplay = args.no_display

print("--------------------------------------")
print("Note : R is for Right, L is for left,\nB is for blank. | is for unary\nAnything else is up to you.")
print("Text in " + bcolors.OKGREEN + "green" + bcolors.ENDC + " is the current index.")
print("--------------------------------------")
print("Starting with : ")
print_band(iterator, current_band[0], current_index, display_inline, display_sleep)
print("Run ...")

while True:
    if not check_maximum or maximum_iteration > 0 and check_maximum:
        next_state()
    else:
        ending(2)
    maximum_iteration -= 1
