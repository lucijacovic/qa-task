from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    cookies = (By.ID, "finansavisen-gdpr-disclaimer-confirm")
    news = (By.XPATH, "//div[@class='c-header-bar-nav__item__content js-header-item-content']") #NE [0]
    # Nyheter[0] and Podcast[1]: same class name, index bad locator practice, but no other option (for now)
    categories = (By.XPATH, "//div[@class='c-header-bar-nav__small-menu js-header-small-menu open']/ul/li")
    categoryName = (By.XPATH, "a/span")

    def acceptCookies(self):
        return self.driver.find_element(*HomePage.cookies)

    def getNews(self):
        return self.driver.find_elements(*HomePage.news) # NE [0]

    def getCategories(self):
        return self.driver.find_elements(*HomePage.categories)

    def getCategoryName(self, categories):
        return categories.find_element(*HomePage.categoryName)
