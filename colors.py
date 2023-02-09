class bcolors:
    """
    bcolor.COLOR to change the printed color
    """
    OKRED = '\33[31m'
    OKGREEN = '\33[32m'
    OKYELLOW = '\33[33m'
    OKBLUE = '\33[34m'
    OKVIOLET = '\33[35m'
    OKBEIGE = '\33[36m'
    OKWHITE = '\33[37m'

    OKBLACKBG = '\33[40m'
    OKREDBG = '\33[41m'
    OKGREENBG = '\33[42m'
    OKYELLOWBG = '\33[43m'
    OKBLUEBG = '\33[44m'
    OKVIOLETBG = '\33[45m'
    OKBEIGEBG = '\33[46m'
    OKWHITEBG = '\33[47m'

    WARNING = '\033[93m'
    FAIL = '\033[91m'

    BOLD = '\033[1m'
    ITALIC = '\33[3m'
    BLINK = '\33[5m'
    UNDERLINE = '\033[4m'

    ENDC = '\033[0m'


color_dict = {
    # Text color
    "red": bcolors.OKRED,
    "green": bcolors.OKGREEN,
    "yellow": bcolors.OKYELLOW,
    "blue": bcolors.OKBLUE,
    "violet": bcolors.OKVIOLET,
    "beige": bcolors.OKBEIGE,
    "white": bcolors.OKWHITE,
    # Background colors
    "black_bg": bcolors.OKBLACKBG,
    "red_bg": bcolors.OKREDBG,
    "green_bg": bcolors.OKGREENBG,
    "yellow_bg": bcolors.OKYELLOWBG,
    "blue_bg": bcolors.OKBLUEBG,
    "violet_bg": bcolors.OKVIOLETBG,
    "beige_bg": bcolors.OKBEIGEBG,
    "white_bg": bcolors.OKWHITEBG,
    # debug colors
    "warning": bcolors.WARNING,
    "fail": bcolors.FAIL,
    # text effect
    "bold": bcolors.BOLD,
    "italic": bcolors.ITALIC,
    "underline": bcolors.UNDERLINE
}


def available_colors():
    print("Available colors : \n -- Text color :")
    i = 0
    for colors in color_dict.keys():
        print(colors, end=", ")
        i += 1
        if i == 6:
            print("\n -- Background color :")
        elif i == 15:
            print("\n -- Debug color :")
        elif i == 17:
            print("\n -- Text effect :")
    print("")
