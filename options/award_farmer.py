from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from seleniumbase import Driver
import randfacts
import requests
import re
import datetime
import time
from config import username, password

# pip install selenium==4.12.0
# pip install seleniumbase

class Awardfarmer:

    def __init__(self, main_url, link):
        self.driver = Driver(uc=True, headless=True)
        self.wait = WebDriverWait(self.driver, 40)
        self.main_url = main_url
        self.username = username

        self.login(username, password)
        self.my_post_key = self.get_post_key()
        self.tid = self.get_tid(link)
        self.bumper()

    # loop to keep bumping all the threads as long as user is logged in
    def bumper(self):
        while True:
            try:
                self.bump()
            except Exception as e:
                print(f"Error: {e}")
                print(f"{datetime.datetime.now().replace(microsecond=0)} : An error occurred. The script continutes...")
                time.sleep(0.5)

    def get_reply_link(self, link):
        self.driver.get(link)
        newreply_xpath = '//*[@id="noa-posttransition"]/div[2]/div/div/a'
        element = self.wait.until(ec.visibility_of_element_located((By.XPATH, newreply_xpath)))
        reply_link = element.get_attribute('href')
        return reply_link
    
    def get_tid(self, link):
        self.driver.get(link)
        html = self.driver.page_source
        tid = re.search(r'name="tid" value="([^"]+)"', html).group(1)
        return tid
    
    def get_post_key(self):
        self.driver.get("https://oguser.com/Thread-Like--753639")
        html = self.driver.page_source
        post_key = re.search(r'my_post_key=([a-f0-9]{32})', html).group(1)
        return post_key

    # try to log in to the website with given user credentials
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

    # check if user is still logged in. return True is he is
    def logged_in(self) -> bool:
        self.driver.get(self.main_url + 'usercp.php')
        time.sleep(2)
        username_xpath = '//*[@id="fullcontainment"]/div[1]/div[2]/div[2]/div/div/div/div/div/div/a[1]'
        elements = self.driver.find_elements(By.XPATH, username_xpath)
        return len(elements) > 0

    # replys random fact under tid
    def bump_old(self):
        self.driver.get(self.reply_link)
        fact = randfacts.get_fact()

        self.wait.until(ec.frame_to_be_available_and_switch_to_it(
            (By.CSS_SELECTOR, 'div.sceditor-container iframe')))
        body = self.wait.until(ec.element_to_be_clickable((By.TAG_NAME, 'body')))
        body.click()
        body.send_keys(fact)
        self.driver.switch_to.default_content()

        button_xpath = '//*[@id="fullcontainment"]/div[1]/form/div[2]/input[1]'
        self.wait.until(ec.element_to_be_clickable((By.XPATH, button_xpath))).click()
        print('SENT: ' + fact)
        time.sleep(7)

    def bump(self):
        fact = randfacts.get_fact()

        cookies = {c['name']: c['value'] for c in self.driver.get_cookies()}

        data = {
            "my_post_key": self.my_post_key,
            "subject": 0,
            "action": "do_newreply",
            "posthash": 0,
            "quoted_ids": "",
            "lastpid": 0,
            "from_page": "1",
            "tid": self.tid,
            "method": "quickreply",
            "message": fact,
        }

        resp = requests.post(
            f"{self.main_url}/newreply.php?tid={self.tid}&processed=1",
            data=data,
            cookies=cookies,
            headers={"User-Agent": self.driver.execute_script("return navigator.userAgent")}
        )

        print(f'SENT: {fact}')
        time.sleep(7)

