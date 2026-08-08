import randfacts
import time

from src.autobumper import Autobumper

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
                print(f"ERROR: {e}")
                time.sleep(0.5)
