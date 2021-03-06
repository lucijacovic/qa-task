from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    cookies = (By.ID, "finansavisen-gdpr-disclaimer-confirm")
    news = (By.XPATH, "//div[@class='c-header-bar-nav__item__content js-header-item-content']")
    dropdownName = (By.XPATH, "//div[@class='c-header-bar-nav__item__content js-header-item-content']/span")
    categories = (By.XPATH, "//div[@class='c-header-bar-nav__small-menu js-header-small-menu open']/ul/li")
    categoryName = (By.XPATH, "a/span")

    news_mobile = (By.XPATH, "//div[@class='c-frontpagemobilenav__dropdown js-subnav-item']")
    # only one dropdown on mobile resolution, no podcast
    dropdownName_mobile = (By.XPATH, "//div[@class='c-frontpagemobilenav__dropdown js-subnav-item']/span")
    categories_mobile = (By.XPATH, "//div[@class='c-frontpagemobilenav__dropdown js-subnav-item toggled']/div/ul/li")
    # categoryName_mobile = (By.XPATH, "a/span") #not needed, same partial xpath

    def acceptCookies(self):
        return self.driver.find_element(*HomePage.cookies)

    def checkDropdownName(self):
        return self.driver.find_element(*HomePage.dropdownName) # takes first element[0]

    def getNews(self):
        return self.driver.find_elements(*HomePage.news)

    def getCategories(self):
        return self.driver.find_elements(*HomePage.categories)

    def getCategoryName(self, categories):
        return categories.find_element(*HomePage.categoryName)

    def checkDropdownNameMobile(self):
        return self.driver.find_element(*HomePage.dropdownName_mobile)

    def getNewsMobile(self):
        return self.driver.find_element(*HomePage.news_mobile)

    def getCategoriesMobile(self):
        return self.driver.find_elements(*HomePage.categories_mobile)

    def getCategoryNameMobile(self, categories_mobile):
        return categories_mobile.find_element(*HomePage.categoryName)
