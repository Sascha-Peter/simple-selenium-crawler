#!/usr/bin/env python

"""This file contains the selenium web crawler and it's logic

@author: Sascha Peter <sascha.o.peter@gmail.com>
@version: 0.1.0-alpha
@since: 2015-11-01
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SeleniumCrawler(object):
    """This class provides the web crawler logic"""

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.country_list = ["Canada"]

    def test(self):
        self.driver.get("http://international.o2.co.uk/internationaltariffs/" +
                        "calling_abroad_from_uk")
        print(self.driver.title)

    def get_tariff_information(self, country):
        """Finds the country input element and searches for the given
        country
        """
        input_element = self.driver.find_element_by_id("countryName")
        input_element.click()
        input_element.send_keys(country)
        input_element.send_keys(Keys.RETURN)
        monthly_element = self.driver.find_element_by_id("paymonthly")
        monthly_element.click()


if __name__ == '__main__':
    crawler = SeleniumCrawler()
    crawler.test()
    crawler.get_tariff_information("Canada")