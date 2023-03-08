"""
Here i'm trying to determine if a state is infinite
My first idea is to check if a state can read everything and don't get ton any other state

"""

def analyse(transition_list, bands):
    """
        analyse the content of the machine to detect divergence

        The input is a dictionnary of transition, such as :
        0: [['|', 'B', 1]],
        1: [['B', 'R', 0]]

        The band is also necessary, to know the complete vocabulary
    """
    possible_values = extract_possible_values(transition_list, bands)
    print("Possible values : ", possible_values)
    state_can_read = {}


def extract_possible_values(transition_list, bands):
    values = []
    for band in bands:
        for car in band:
            if car not in values:
                values.append(car)

    for my_list in transition_list.values():
        # [['|', 'R', 'B', '2'], ['B', 'N', 'B', '3']],
        for sublist in my_list:
            for elem in sublist[:-1]:  # don't check last element as it's the next step
                if elem not in values:
                    values.append(elem)
    return values

