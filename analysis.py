def analyse(transition_list, band):
    """
        analyse the content of the machine to detect divergence

        The input is a dictionnary of transition, such as :
        0: [['|', 'B', 1]],
        1: [['B', 'R', 0]]

        The band is also necessary, to know the complete vocabulary
    """
    extract_possible_values(transition_list, band)
    pass


def extract_possible_values(transition_list, band):
    values = []
    for car in band:
        if car not in values:
            values.append(car)
    for my_list in transition_list.values():
        # [['|', 'R', 'B', '2'], ['B', 'N', 'B', '3']],
        for sublist in my_list:
            for elem in sublist[:-1]:  # don't check last element as it's the next step
                if elem not in values:
                    values.append(elem)
    print(values)
    pass
