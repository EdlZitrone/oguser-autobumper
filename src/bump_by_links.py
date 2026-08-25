import time

from src.autobumper import Autobumper

class LinkBumper(Autobumper):

    def __init__(self, headless):
        super().__init__(headless)

        links = self.get_links()
        self.tids = [ self.get_tid(link) for link in links ]
        self.titles = [ self.get_title(link) for link in links ]
        
        self.bumper()

    def bumper(self):
        while True:
            if not self.is_driver_alive():
                print("STATUS: Browser session lost. Restarting driver...")
                self.restart_driver()

            if not self.is_logged_in():
                print("STATUS: Not logged in. Trying to log in again...")
                self.login()
                self.update_post_key()

            for i in range(len(self.tids)):
                try:
                    self.newreply(self.tids[i], self.titles[i])
                    time.sleep(11)
                except Exception as e:
                    print(f"ERROR: {e}")
                    time.sleep(0.5)
            print('Finished bumping all threads!')
            time.sleep(4*1800 - len(self.tids)*0)

    def get_links(self):
        links = []
        with open('threads.txt') as file:
            for line in file:
                links.append(line.split("\n")[0])
        return links