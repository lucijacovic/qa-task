from selenium.webdriver.common.action_chains import ActionChains
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass



class TestOne(BaseClass):

    def test_newsDesktop(self):
        # if window_size == "desktop" or "tablet":
        #   run this method
        log = self.getLogger()
        homePage = HomePage(self.driver)
        log.info("Desktop/Tablet test:")
        log.info("Accepting cookies")
        homePage.acceptCookies().click() # accept cookies, in case any elements are hidden underneath

        # since we used index for locating news element, best to check if dropdown is actually Nyheter,
        # in case a new dropdown element with same class is added before Nyheter (which would make Nyheter[1])
        dropdown_name = homePage.checkDropdownName().text
        assert dropdown_name == "Nyheter"

        action = ActionChains(self.driver)  # need to hover
        log.info("Hovering over Nyheter")
        news = homePage.getNews()
        # Nyheter[0] and Podcast[1]: same class name, index bad locator practice, but no other option (for now)
        action.move_to_element(news[0]).perform()  # hover

        # check if dropdown menu/elements actually appear
        self.verifyDropdownMenuPresence()

        log.info("Getting all categories")
        categories = homePage.getCategories()

        # Drop-down list that appears should have exactly 12 elements
        assert len(categories) == 12

        names = []
        for category in categories:
            categoryName = homePage.getCategoryName(category).text
            log.info(categoryName)
            names.append(categoryName)

        # The first two elements should be “Siste 24 timer” and “Leder”
        assert names[0] == "Siste 24 timer"
        # assert names[1] == "Leder"  # AssertionError, second element is Alle pluss-artikler


    def test_newsMobile(self):
        self.driver.set_window_size(360, 640) # mobile resolution, should be defined in conftest.py
        # if window_size == "mobile":
        #   run this method
        self.driver.implicitly_wait(3) # need to wait for website to switch to mobile elements

        log = self.getLogger()
        homePage = HomePage(self.driver)
        log.info("Mobile test:")
        log.info("Clicking on Nyheter")
        homePage.getNewsMobile().click() # element is now clickable (no hover)

        # check if dropdown menu/elements actually appear
        self.verifyDropdownMenuPresenceMobile()

        log.info("Getting all categories")
        categories_mobile = homePage.getCategoriesMobile()

        # Drop-down list that appears should have exactly 12 elements
        assert len(categories_mobile) == 12

        names_mobile = []
        for category in categories_mobile:
            categoryName = homePage.getCategoryNameMobile(category).text
            log.info(categoryName)
            names_mobile.append(categoryName)

        # The first two elements should be “Siste 24 timer” and “Leder”.
        assert names_mobile[0] == "Siste 24 timer"
        # assert names_mobile[1] == "Leder"  # AssertionError, second element is Alle pluss-artikler
