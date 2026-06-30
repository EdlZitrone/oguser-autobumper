import requests
import time
import re

from abc import ABC, abstractmethod

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from seleniumbase import Driver

from config import username, password

class Autobumper(ABC):

    def __init__(self, headless) -> None:
        self.main_url = "https://oguser.com/"
        self.username = username
        self.driver = Driver(uc=True, headless=headless)
        self.wait = WebDriverWait(self.driver, 40)

        self.login(username, password)
        self.my_post_key = self.get_post_key()

    @abstractmethod
    def bumper(self):
        pass

    def get_post_key(self):
        self.driver.get("https://oguser.com/Thread-Like--753639")
        html = self.driver.page_source
        post_key = re.search(r'my_post_key=([a-f0-9]{32})', html).group(1)
        return post_key
    
    def get_tid(self, link):
        if self.driver.current_url != link:
            self.driver.get(link)
        html = self.driver.page_source
        tid = re.search(r'name="tid" value="([^"]+)"', html).group(1)
        return tid
    
    def get_title(self, link):
        if self.driver.current_url != link:
            self.driver.get(link)
        title_xpath = '/html/body/div[8]/div/div[1]/span'
        title_element = self.wait.until(ec.visibility_of_element_located((By.XPATH, title_xpath)))

        title = self.driver.execute_script(
            "return Array.from(arguments[0].childNodes)"
            ".filter(n => n.nodeType === 3).map(n => n.textContent).join('');",
            title_element
        )
        return title.replace('\xa0', ' ').strip().upper()
    
    def get_tid_and_title(self, link):
        tid = self.get_tid(link)
        title = self.get_title(link)
        return tid, title
    
    def login(self, username, password):
        self.driver.get('https://google.com')
        self.driver.set_window_size(600, 600)
        time.sleep(3)
        self.driver.get(self.main_url)
        time.sleep(7)
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[1]/div[3]/a'))).click()
        user_xpath = '//*[@id="fullcontainment"]/div/form[2]/table/tbody/tr[1]/td/label/input'
        self.wait.until(ec.visibility_of_element_located((By.XPATH, user_xpath))).send_keys(username)
        pass_xpath = '//*[@id="fullcontainment"]/div/form[2]/table/tbody/tr[2]/td/label/input'
        self.wait.until(ec.visibility_of_element_located((By.XPATH, pass_xpath))).send_keys(password)
        login_xpath = '//*[@id="fullcontainment"]/div/form[2]/table/tbody/tr[4]/td/span/input'
        self.wait.until(ec.visibility_of_element_located((By.XPATH, login_xpath))).click()
        profile_xpath = '//*[@id="dropdown-profile-mobile"]'
        self.wait.until(ec.visibility_of_element_located((By.XPATH, profile_xpath)))
        print("Status: Logged in.")

    def newreply(self, tid, message):
      cookies = {c['name']: c['value'] for c in self.driver.get_cookies()}

      data = {
          "my_post_key": self.my_post_key,
          "subject": 0,
          "action": "do_newreply",
          "posthash": 0,
          "quoted_ids": "",
          "lastpid": 0,
          "from_page": "1",
          "tid": tid,
          "method": "quickreply",
          "message": message,
      }

      requests.post(
          f"{self.main_url}/newreply.php?tid={tid}&processed=1",
          data=data,
          cookies=cookies,
          headers={"User-Agent": self.driver.execute_script("return navigator.userAgent")}
      )

      print(f'SENT: {message}')