"""This file contains the selenium web crawler and it's logic

@author: Sascha Peter <sascha.o.peter@gmail.com>
@version: 0.1.0-alpha
@since: 2015-11-01
"""

from selenium import webdriver


class SeleniumCrawler(object):
    """This class provides the web crawler logic"""

    def __init__(self):
        self.driver = webdriver.Firefox()

    def test(self):
        self.driver.get("http://international.o2.co.uk/internationaltariffs/calling_abroad_from_uk")
        print(self.driver.title)


if __name__ == '__main__':
    crawler = SeleniumCrawler()
    crawler.test()
