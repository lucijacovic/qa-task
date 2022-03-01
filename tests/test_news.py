from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_news(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)

        log.info("Accepting cookies")
        homePage.acceptCookies().click() # accept cookies, in case any elements are hidden underneath

        action = ActionChains(self.driver)  # need to hover
        log.info("Hovering over Nyheter")
        news = homePage.getNews()
        action.move_to_element(news[0]).perform()  # hover

        log.info("Getting all categories")
        categories = homePage.getCategories()
        names = []
        for category in categories:
            categoryName = homePage.getCategoryName(category).text
            log.info(categoryName)
            names.append(categoryName)

        # Drop-down list that appears should have exactly 12 elements and
        # the first two should be “Siste 24 timer” and “Leder”.

        assert len(categories) == 12
        assert names[0] == "Siste 24 timer"
        assert names[1] == "Leder"  # AssertionError, second element is Alle pluss-artikler

# to do: implement testing different resolutions(desktop, tablet, mobile)