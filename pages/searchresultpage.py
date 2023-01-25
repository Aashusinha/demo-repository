from selenium.webdriver.common.by import By

from base.basepage import BaseDriver


class Searchresults(BaseDriver):
    def __int__(self,driver):
        super().__int__(driver)
        self.driver=driver

    def Filter(self):
        self.driver.find_element(By.XPATH, "(//p[@class='font-lightgrey bold'])[2]").click()