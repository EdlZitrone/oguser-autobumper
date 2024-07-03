from options import Awardfarmer, LinkBumper, ProfileBumper

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

class OguserBumper:

    def __init__(self) -> None:
        self.main_url = "https://oguser.com/"
        self.header()
        self.menu()

    def header(self) -> None:
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

    def menu(self):
        print(bcolors.WARNING + "[1] Autobumper by threads from profile." + bcolors.ENDC)
        print(bcolors.WARNING + "[2] Autobumper by threads from threads.txt." + bcolors.ENDC)
        print(bcolors.WARNING + "[3] Awardfarmer by thread link input." + bcolors.ENDC)
        print(bcolors.WARNING + "[4] Exit OGU Bumper." + bcolors.ENDC)
        mode = input(bcolors.HEADER + "\nEnter the number of the preferred option: " + bcolors.ENDC)

        if (mode == '1'):
            print(bcolors.WARNING + "\nStarting Autobumper..." + bcolors.ENDC)
            ProfileBumper(main_url=self.main_url)
        elif (mode == '2'):
            print(bcolors.WARNING + "\nStarting Autobumper..." + bcolors.ENDC)
            LinkBumper(main_url=self.main_url)
        elif (mode == '3'):
            link = input(bcolors.HEADER + "Enter link to Farming thread: " + bcolors.ENDC)
            print(bcolors.WARNING + "\nStarting Awardfarmer..." + bcolors.ENDC)
            Awardfarmer(main_url=self.main_url, link=link)
        elif (mode == '4'):
            print(bcolors.WARNING + "\nExiting OGU Bumper..." + bcolors.ENDC)
        else:
            print(bcolors.WARNING + "\nPlease chose one of the options above." + bcolors.ENDC)
            self.menu()

if (__name__ == '__main__'):
    OguserBumper()