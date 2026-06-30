import datetime
import time

from options.autobumper import Autobumper

class LinkBumper(Autobumper):

    def __init__(self):
        super().__init__()

        links = self.get_links()
        self.tids = [ self.get_tid(link) for link in links ]
        self.titles = [ self.get_title(link) for link in links ]
        
        self.bumper()

    def bumper(self):
        while True:
            for i in range(len(self.tids)):
                try:
                    self.newreply(self.tids[i], self.titles[i])
                    time.sleep(7)
                except Exception as e:
                    print(f"Error: {e}")
                    print(f"{datetime.datetime.now().replace(microsecond=0)} : An error occurred. The script continutes...")
                    time.sleep(0.5)
            print('Finished bumping all threads!')
            time.sleep(4*1800 - len(self.tids)*7)

    def get_links(self):
        links = []
        with open('threads.txt') as file:
            for line in file:
                links.append(line.split("\n")[0])
        return links