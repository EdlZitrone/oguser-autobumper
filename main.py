import argparse

from src import Awardfarmer, LinkBumper, ProfileBumper

def str2bool(value):
    if isinstance(value, bool):
        return value
    if value.lower() in ('true', '1', 'yes', 'y'):
        return True
    elif value.lower() in ('false', '0', 'no', 'n'):
        return False
    raise argparse.ArgumentTypeError('Boolean value expected (true/false).')

def parse_args():
    parser = argparse.ArgumentParser(description="OGU Bumper - A lightweight Autobumper and Awardfarmer (Events) for https://oguser.com written in Python.")
    parser.add_argument('--headless', type=str2bool, default=True,
                         help="Run browser in headless mode (default: True)")
    parser.add_argument('--mode', type=int, default=None,
                         help="Bumper mode to run without the interactive menu: 1 (profile), 2 (threads.txt), 3 (award farmer). Falls back to the interactive prompt if omitted or not one of 1/2/3.")
    parser.add_argument('--thread', type=str, default=None,
                        help="Link to the thread to be farmed (only used with option 3, award farmer).")
    return parser.parse_args()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def header():
    print("\033[H\033[J", end="")
    header = bcolors.HEADER + '''
 ▒█████    ▄████  █    ██     ▄▄▄▄    █    ██  ███▄ ▄███▓ ██▓███  ▓█████  ██▀███  
▒██▒  ██▒ ██▒ ▀█▒ ██  ▓██▒   ▓█████▄  ██  ▓██▒▓██▒▀█▀ ██▒▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒
▒██░  ██▒▒██░▄▄▄░▓██  ▒██░   ▒██▒ ▄██▓██  ▒██░▓██    ▓██░▓██░ ██▓▒▒███   ▓██ ░▄█ ▒
▒██   ██░░▓█  ██▓▓▓█  ░██░   ▒██░█▀  ▓▓█  ░██░▒██    ▒██ ▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  
░ ████▓▒░░▒▓███▀▒▒▒█████▓    ░▓█  ▀█▓▒▒█████▓ ▒██▒   ░██▒▒██▒ ░  ░░▒████▒░██▓ ▒██▒
░ ▒░▒░▒░  ░▒   ▒ ░▒▓▒ ▒ ▒    ░▒▓███▀▒░▒▓▒ ▒ ▒ ░ ▒░   ░  ░▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
  ░ ▒ ▒░   ░   ░ ░░▒░ ░ ░    ▒░▒   ░ ░░▒░ ░ ░ ░  ░      ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░
░ ░ ░ ▒  ░ ░   ░  ░░░ ░ ░     ░    ░  ░░░ ░ ░ ░      ░   ░░          ░     ░░   ░ 
    ░ ░        ░    ░         ░         ░            ░               ░  ░   ░     
                                   ░                                              
                                                                    oguser.com/mf''' + bcolors.ENDC
    print(header + '\n')

def menu(args):
    print(bcolors.WARNING + "[1] Autobumper by threads from profile." + bcolors.ENDC)
    print(bcolors.WARNING + "[2] Autobumper by threads from threads.txt." + bcolors.ENDC)
    print(bcolors.WARNING + "[3] Awardfarmer by thread link input." + bcolors.ENDC)
    print(bcolors.WARNING + "[4] Exit OGU Bumper." + bcolors.ENDC)

    if args.mode is not None and args.mode in (1, 2, 3):
        mode = str(args.mode)
    else:
        mode = input(bcolors.HEADER + "\nEnter the number of the preferred option: " + bcolors.ENDC)

    if mode == '1':
        print(bcolors.WARNING + "\nStarting Autobumper..." + bcolors.ENDC)
        ProfileBumper(headless=args.headless)
    elif mode == '2':
        print(bcolors.WARNING + "\nStarting Autobumper..." + bcolors.ENDC)
        LinkBumper(headless=args.headless)
    elif mode == '3':
        if args.thread is not None:
            thread = str(args.thread)
        else:
            thread = input(bcolors.HEADER + "Enter link to Farming thread: " + bcolors.ENDC)
        print(bcolors.WARNING + "\nStarting Awardfarmer..." + bcolors.ENDC)
        Awardfarmer(link=thread, headless=args.headless)
    elif mode == '4':
        print(bcolors.WARNING + "\nExiting OGU Bumper..." + bcolors.ENDC)
    else:
        print(bcolors.WARNING + "\nPlease chose one of the options above." + bcolors.ENDC)
        menu(args)

if __name__ == '__main__':
    args = parse_args()
    header()
    menu(args)