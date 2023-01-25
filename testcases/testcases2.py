from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_Automation.pages.launchpage import LaunchPage
from pages.searchresultpage import Searchresults
from base.basepage import BaseDriver


@pytest.mark.usefixtures('setup')
class Test_script:
    def test_function(self):

    # launch browser and launching the website



    # provide depart from location

        lp=LaunchPage(self.driver)
        lp.departFrom('new delhi')


    # provide going location
        lp.goingTo('new')



        # to select the departure date
        lp.departuredate('21/01/2023')

    # click on flight search button

        lp.searchButton()


        self.driver.set_page_load_timeout(100)
        self.driver.get('https://flight.yatra.com/air-search-ui/dom2/trigger?type=O&viewName=normal&flexi=0&noOfSegments=1&origin=DEL&originCountry=IN&destination=BOM&destinationCountry=IN&flight_depart_date=10%2F01%2F2023&ADT=1&CHD=0&INF=0&class=Economy&source=fresco-home&unqvaldesktop=1012116628059')
        ele=self.driver.find_element(By.XPATH,"(//p[@class='font-lightgrey bold'])[2]")
        self.wait.until(EC.visibility_of(ele))

    # to handel dynamic scroll button
        bp=BaseDriver(self.driver)
        bp.scrollButton()

        # select the filter one stop

        sp = Searchresults(self.driver)
        sp.Filter()


        all_stops=bp.wait_until_presence_all_element_located(By.XPATH,"//span[@class='dotted-borderbtm']")
        print(len(all_stops))


     # verify that filtered results having 1 stop

        for i in all_stops:

            assert i.text == "1 Stop"
            print('assert pass')
        sleep(4)
