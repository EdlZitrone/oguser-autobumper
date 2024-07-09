from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from seleniumbase import Driver
import randfacts
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
        self.reply_link = self.get_reply_link(link)
        self.bumper()

    # loop to keep bumping all the threads as long as user is logged in
    def bumper(self):
        while True:
            try:
                self.bump
            except Exception as e:
                print(f"{datetime.datetime.now().replace(microsecond=0)} : An error occurred. The script continutes...")

    def get_reply_link(self, link):
        self.driver.get(link)
        newreply_xpath = '//*[@id="noa-posttransition"]/div[2]/div/div/a'
        element = self.wait.until(ec.visibility_of_element_located((By.XPATH, newreply_xpath)))
        reply_link = element.get_attribute('href')
        return reply_link

    # try to log in to the website with given user credentials
    def login(self, username, password):
        self.driver.get('https://google.com')
        self.driver.set_window_size(600, 600)
        time.sleep(3)
        self.driver.execute_script(f"window.open('{self.main_url}', '_blank')")
        time.sleep(7)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.get(self.main_url + 'login')
        user_xpath = '//*[@id="fullcontainment"]/div/form[2]/table/tbody/tr[1]/td/label/input'
        self.wait.until(ec.visibility_of_element_located((By.XPATH, user_xpath))).send_keys(username)
        pass_xpath = '//*[@id="fullcontainment"]/div/form[2]/table/tbody/tr[2]/td/label/input'
        self.wait.until(ec.visibility_of_element_located((By.XPATH, pass_xpath))).send_keys(password)
        login_xpath = '//*[@id="fullcontainment"]/div/form[2]/table/tbody/tr[4]/td/span/input'
        self.wait.until(ec.visibility_of_element_located((By.XPATH, login_xpath))).click()
        time.sleep(10)

    # check if user is still logged in. return True is he is
    def logged_in(self) -> bool:
        self.driver.get(self.main_url + 'usercp.php')
        time.sleep(2)
        username_xpath = '//*[@id="fullcontainment"]/div[1]/div[2]/div[2]/div/div/div/div/div/div/a[1]'
        elements = self.driver.find_elements(By.XPATH, username_xpath)
        return len(elements) > 0

    # replys random fact under tid
    def bump(self):
        self.driver.get(self.reply_link)
        fact = randfacts.get_fact()
        self.wait.until(ec.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe')))
        self.wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body'))).send_keys(fact)
        self.driver.switch_to.default_content()
        button_xpath = '//*[@id="fullcontainment"]/div[1]/form/div[2]/input[1]'
        self.wait.until(ec.element_to_be_clickable((By.XPATH, button_xpath))).click()
        print('SENT: ' + fact)
        time.sleep(7)