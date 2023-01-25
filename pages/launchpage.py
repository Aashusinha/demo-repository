from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.basepage import BaseDriver


class LaunchPage(BaseDriver):
    def __init__(self,driver):
        super().__int__(driver)
        self.driver=driver

    def departFrom(self,departfrom):
            #depart_from = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@name='flight_origin'])[1]")))
            depart_from=self.wait_until_element_to_be_clickable(By.XPATH, "(//input[@name='flight_origin'])[1]")
            depart_from.click()
            depart_from.send_keys(departfrom)
            depart_from.send_keys(Keys.ENTER)



    def goingTo(self,goingto):
            going_to = self.wait_until_element_to_be_clickable("(//input[@id='BE_flight_arrival_city'])")
            going_to.click()
            going_to.send_keys('new')
            search_results = self.wait_until_presence_all_element_located("//div[@class='viewport']/div/div/li")
            for result in search_results:
                if 'New York (LGA)' in result.text:
                    result.click()
                    break


    def departuredate(self,departuredate):
            bp=BaseDriver(self.driver)
            bp.wait_until_element_to_be_clickable(By.XPATH, "//input[@id='BE_flight_origin_date']").click()
            all_dates = bp.wait_until_element_to_be_clickable(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']") \
                .find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
            for date in all_dates:
                if date.get_attribute('data-date') == '22/01/2023':
                    date.click()
                    break

    def searchButton(self):
             self.driver.find_element(By.XPATH,"//input[@id='BE_flight_flsearch_btn' and @value='Search Flights']").click()
             sleep(4)