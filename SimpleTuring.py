import sys
import argparse

''' Content of the help :
usage: main.py [-h] [-b BAND] [-i INT [INT ...]] [-s START_INDEX] [-d DICTIONARY [DICTIONARY ...]] -t TRANSITIONS [TRANSITIONS ...]

options:
  -h, --help            show this help message and exit
  -b BAND, --band BAND  Starting band for the program
  -i INT [INT ...], --int INT [INT ...]
                        integers to add to the band
  -s START_INDEX, --start-index START_INDEX
                        Starting index of the machine
  -d DICTIONARY [DICTIONARY ...], --dictionary DICTIONARY [DICTIONARY ...]
                        Define the dictionary (format : A B C | D )
  -t TRANSITIONS [TRANSITIONS ...], --transitions TRANSITIONS [TRANSITIONS ...]
                        Transitions (format : '<start state> <read> <action> <end state>' Example : "0 B | 1" "0 | | 0"
Usage Example : 
python SimpleTuring.py -t "0 | B 1" "0 B B 0" "1 B R 0" -i 2 3
'''

current_band = ""
current_index = 0
current_state = 0
iterator = 0

#################################
# ADD YOUR CUSTOM MACHINES HERE #
cleaner = {
    0: [['|', 'B', 1]],
    1: [['B', 'R', 0]]
}

startAndEnd = {
    0: [['|', 'L', 1]],
    1: [['B', 'S', 1], ['S', 'R', 2]],
    2: [['|', 'R', 2], ['B', 'R', 3]],
    3: [['|', 'R', 2], ['B', 'E', 4]],
    4: [['E', 'L', 5]],
    5: [['B', 'L', 5], ['|', 'L', 5], ['S', 'S', 6]],
}

maximum = {
    0: [['|', 'L', 1]],
    1: [['B', 'S', 1], ['S', 'R', 2]],
    2: [['|', 'R', 2], ['B', 'R', 3]],
    3: [['|', 'R', 2], ['B', 'E', 4]],
    4: [['E', 'L', 5]],
    5: [['B', 'L', 5], ['|', 'L', 51], ['O', 'L', 5], ['S', 'R', 56]],
    51: [['|', 'L', 51], ['O', 'L', 52], ['B', 'L', 52], ['S', 'S', 57]],
    52: [['B', 'L', 52], ['O', 'L', 52], ['|', 'L', 53], ['S', 'S', 57]],
    53: [['|', 'L', 53], ['O', 'L', 53], ['B', 'L', 53], ['S', 'R', 6]],
    6: [['O', 'R', 6], ['|', 'O', 7], ['B', 'R', 6], ['E', 'E', 4]],
    7: [['O', 'R', 7], ['|', 'R', 7], ['B', 'R', 6]],
    57: [['S', 'R', 57], ['B', 'R', 57], ['O', 'R', 57], ['E', 'E', 57], ['|', 'L', 58]],
    58: [['O', '|', 58], ['|', 'L', 58], ['B', 'B', 58], ['B', 'R', 59]],
    59: [['|', 'B', 59], ['B', 'B', 59]],
}

# Don't forget to add it below !
machines = {
    "cleaner": cleaner,
    "maximum": maximum
}

# ## END OF CUSTOM MACHINES  ## #
#################################

class bcolors:
    """
    bcolor.COLOR to change the printed color
    """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def make_machine(transitions):
    """
    create the dictionary representation of the machine from the transition in arguments
    :param transitions: a list_integ of string in the format "<start state> <read> <action> <end state>"
    """
    try:
        my_dict = {}
        for elem in transitions:
            current = elem.split(' ')
            state = int(current[0])
            if not my_dict.get(state):
                my_dict[
                    state] = []  # dictionary of the form : <start state>: [ [<read>, <action>, <end state>], [...]]
            my_dict.get(state).append([current[1], current[2], int(current[3])])
        global machine
        machine = my_dict
    except Exception as ex:
        error("Exception caught during machine creation :\n{}".format(ex))


def print_human():
    """
    Print the current machine as a human readable format, then exits
    """
    sorted_dict = dict(sorted(machine.items()))
    for key in sorted_dict.keys():
        for elem in sorted_dict.get(key):
            print("{}  {}  {}  {}".format(key, elem[0], elem[1], elem[2]))
        # print("\t{}: {},".format(key, machine.get(key)))


def print_machine(name):
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


def init_band(integers, band):
    """
    Initialize the Machine's memory or "band"
    :param integers: a list_integ of integers
    :param band: a string containing a custom band
    """
    global current_band
    current_band = band
    current_band += "BBB"
    global current_index
    current_index += 3  # because I add BBB for clarity
    current_band += add_integers(integers)
    current_band += "BBB"


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


def print_state(action):
    """
    Print the current band, index, state, action (for debugging purpose)
    :param action: the last action (it's not a global)
    """
    print("Band : {}\nIndex : {}\nState : {}\nLast Action : {}".format(current_band, current_index, current_state,
                                                                       action))


def print_band(etat = None):
    """
    Print the current band, with green current index
    """
    my_str = "[" + str(iterator) + "] "
    for i in range(0, len(current_band)):
        if i == current_index:
            my_str += bcolors.OKGREEN + current_band[i] + bcolors.ENDC  # don't forget ENDC !
        else:
            my_str += current_band[i]
    if etat is not None:
        my_str += " -- "+str(etat)
    print(my_str)


def ending(i=0):
    """
    Print the ending infos and exits
    :param i: set to 1 if it was called in the transition exception screen
    """
    print("-----------------\nEnd Reached\nReturn value : ", current_band.count('|'))
    print("Reached in {} steps".format(iterator))
    if i != 0:
        print("Note : Ended because of unknown transition")
    sys.exit(1)


def error(string):
    """
    Print a red string
    :param string: the string to print
    """
    print(bcolors.FAIL + string + bcolors.ENDC)
    sys.exit(1)


def next_state():
    """
    Calculates the next state, from the current state
    """
    global current_index
    global current_state
    global current_band

    current_char = current_band[current_index]  # character pointed by index
    possibilities = machine.get(current_state)  # possible transitions
    machine_step = []
    try:
        for i in range(0, len(possibilities)):
            if possibilities[i][0] == current_char:
                machine_step = possibilities[i]
    except Exception as exp:
        # no possible transition was found -> End
        ending(1)

    if machine_step[1] == 'R':  # move right
        current_index += 1
    elif machine_step[1] == 'L':  # move left
        current_index -= 1
    else:  # replace by character instead of moving
        if current_state == machine_step[2] and machine_step[0] == machine_step[1]:
            ending()
        band = list(current_band)
        band[current_index] = machine_step[1]
        current_band = "".join(band)  # modify the band
    current_state = machine_step[2]  # update current state
    global iterator
    iterator += 1
    print_band(current_state)


# Parse arguments
parser = argparse.ArgumentParser()

parser.add_argument('-b', '--band', help="Starting band for the program",
                    default="", type=str)
parser.add_argument('-i', '--int', help="integers to add to the band", type=int, nargs='+')
parser.add_argument('-s', '--start-index', help="Starting index of the machine", type=int, default=0)
parser.add_argument('-p', '--print', help="Print a python version of the machine, to add it in the code, "
                                          "line 27 and below", type=str)
parser.add_argument('-ph', '--print-human', help="Print the current machine as a human readable format", action='store_true')
parser.add_argument('-m', '--machine', help="Use a custom machine previously added to the source code above,"
                                            " line 27 and below", type=str)

parser.add_argument('-d', '--dictionary', help="Define the dictionary (format : A B C | D )", nargs='+')
parser.add_argument('-t', '--transitions', help="Transitions (format : '<start state> <read> <action> <end state>'\n"
                                                "Example : \"0 B | 1\" \"0 | | 0\"", type=str, nargs='+')
args = parser.parse_args()

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
    current_index = args.startindex
if args.print:
    print_machine(args.print)
if args.print_human:
    print_human()
    sys.exit(1)

print("--------------------------------------")
print("Note : R is for Right, L is for left,\nB is for blank. | is for unary\nAnything else is up to you.")
print("Text in " + bcolors.OKGREEN + "green" + bcolors.ENDC + " is the current index.")
print("--------------------------------------")
print("Starting with : ")
print_band()
print("Run ...")

while True:
    next_state()
