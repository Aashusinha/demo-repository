
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


class BaseDriver:
    def __int__(self,driver):
        self.driver=driver

    def scrollButton(self):
        previous = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
            sleep(3)
            new_height = self.driver.execute_script('return document.body.scrollHeight')
            if new_height == previous:
                break
            previous = new_height
        sleep(3)

    def wait_until_element_to_be_clickable(self,locatorType,locator):
        element=self.wait_until(EC.presence_of_all_elements_located((locatorType,locator)))


    def wait_until_presence_all_element_located(self,locatortype,locator):
        element=self.wait.until(EC.presence_of_all_elements_located((locatortype,locator)))