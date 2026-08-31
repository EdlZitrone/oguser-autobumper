import time

from selenium.webdriver.common.by import By

from src.autobumper import Autobumper

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
            time.sleep(4*1800 - len(self.tids)*5)

    def get_links(self):
        self.driver.get(self.main_url + self.username)
        elements = self.driver.find_elements(By.CLASS_NAME, 'shop_background')
        links = []
        for e in elements:
            link_element = e.find_element(By.CSS_SELECTOR, 'a')
            links.append(link_element.get_attribute('href'))
        return links
