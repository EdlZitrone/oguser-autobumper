from options.award_farmer import Awardfarmer
from options.bump_by_links import LinkBumper
from options.bump_by_profile import ProfileBumper

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

class Flipdbumper:

    def __init__(self) -> None:
        self.header()
        self.menu()

    def header(self) -> None:
        print("\033[H\033[J", end="")
        header = bcolors.HEADER + '''
  █████▒██▓     ██▓ ██▓███  ▓█████▄  ▄▄▄▄    █    ██  ███▄ ▄███▓ ██▓███  ▓█████  ██▀███  
▓██   ▒▓██▒    ▓██▒▓██░  ██▒▒██▀ ██▌▓█████▄  ██  ▓██▒▓██▒▀█▀ ██▒▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒
▒████ ░▒██░    ▒██▒▓██░ ██▓▒░██   █▌▒██▒ ▄██▓██  ▒██░▓██    ▓██░▓██░ ██▓▒▒███   ▓██ ░▄█ ▒
░▓█▒  ░▒██░    ░██░▒██▄█▓▒ ▒░▓█▄   ▌▒██░█▀  ▓▓█  ░██░▒██    ▒██ ▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  
░▒█░   ░██████▒░██░▒██▒ ░  ░░▒████▓ ░▓█  ▀█▓▒▒█████▓ ▒██▒   ░██▒▒██▒ ░  ░░▒████▒░██▓ ▒██▒
 ▒ ░   ░ ▒░▓  ░░▓  ▒▓▒░ ░  ░ ▒▒▓  ▒ ░▒▓███▀▒░▒▓▒ ▒ ▒ ░ ▒░   ░  ░▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
 ░     ░ ░ ▒  ░ ▒ ░░▒ ░      ░ ▒  ▒ ▒░▒   ░ ░░▒░ ░ ░ ░  ░      ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░
 ░ ░     ░ ░    ▒ ░░░        ░ ░  ░  ░    ░  ░░░ ░ ░ ░      ░   ░░          ░     ░░   ░ 
           ░  ░ ░              ░     ░         ░            ░               ░  ░   ░     
                             ░            ░                                              
                                                                    flipd.gg/mf''' + bcolors.ENDC
        print(header + '\n')

    def menu(self):
        print(bcolors.WARNING + "[1] Autobumper by threads from profile." + bcolors.ENDC)
        print(bcolors.WARNING + "[2] Autobumper by threads from threads.txt." + bcolors.ENDC)
        print(bcolors.WARNING + "[3] Awardfarmer by thread link input." + bcolors.ENDC)
        print(bcolors.WARNING + "[4] Exit Flipdbumper." + bcolors.ENDC)
        mode = input(bcolors.HEADER + "\nEnter the number of the preferred option: " + bcolors.ENDC)

        if (mode == '1'):
            print(bcolors.WARNING + "\nStarting Autobumper..." + bcolors.ENDC)
            ProfileBumper()
        elif (mode == '2'):
            print(bcolors.WARNING + "\nStarting Autobumper..." + bcolors.ENDC)
            LinkBumper()
        elif (mode == '3'):
            link = input(bcolors.HEADER + "Enter link to Farming thread: " + bcolors.ENDC)
            print(bcolors.WARNING + "\nStarting Awardfarmer..." + bcolors.ENDC)
            Awardfarmer(link)
        elif (mode == '4'):
            print(bcolors.WARNING + "\nExiting Flipd Bumper..." + bcolors.ENDC)
        else:
            print(bcolors.WARNING + "\nPlease chose one of the options above." + bcolors.ENDC)
            self.menu()

if (__name__ == '__main__'):
    Flipdbumper()