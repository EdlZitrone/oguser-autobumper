import randfacts
import datetime
import time

from options.autobumper import Autobumper

class Awardfarmer(Autobumper):

    def __init__(self, link, headless):
        super().__init__(headless)

        self.tid = self.get_tid(link)
        self.bumper()

    def bumper(self):
        while True:
            try:
                fact = randfacts.get_fact()
                self.newreply(self.tid, fact)
                time.sleep(7)
            except Exception as e:
                print(f"Error: {e}")
                print(f"{datetime.datetime.now().replace(microsecond=0)} : An error occurred. The script continutes...")
                time.sleep(0.5)
