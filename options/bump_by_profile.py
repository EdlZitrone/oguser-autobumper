import datetime
import time

from selenium.webdriver.common.by import By

from options.autobumper import Autobumper

class ProfileBumper(Autobumper):

    def __init__(self, headless):
        super().__init__(headless)

        links = self.get_links()
        results = [self.get_tid_and_title(link) for link in links]
        self.tids = [tid for tid, _ in results]
        self.titles = [title for _, title in results]

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
        self.driver.get(self.main_url + self.username)
        elements = self.driver.find_elements(By.CLASS_NAME, 'shop_background')
        links = []
        for e in elements:
            link_element = e.find_element(By.CSS_SELECTOR, 'a')
            links.append(link_element.get_attribute('href'))
        return links