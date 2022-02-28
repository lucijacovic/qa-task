from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe") # local path

driver.get("https://finansavisen.no/")
driver.maximize_window()

driver.find_element_by_id(
    "finansavisen-gdpr-disclaimer-confirm").click()  # accept cookies, in case any elements are hidden underneath

action = ActionChains(driver)  # need to hover
news = driver.find_elements_by_css_selector(
    # Nyheter[0] and Podcast[1]: same class name, index bad locator practice, but no other option (for now)
    "div[class='c-header-bar-nav__item__content js-header-item-content']")[0]
action.move_to_element(news).perform()  # hover

categories = driver.find_elements_by_xpath(
    "//div[@class='c-header-bar-nav__small-menu js-header-small-menu open']/ul/li")

names = []
for category in categories:
    categoryName = category.find_element_by_xpath("a/span").text
    names.append(categoryName)

# Drop-down list that appears should have exactly 12 elements and
# the first two should be “Siste 24 timer” and “Leder”.

assert len(categories) == 12
assert names[0] == "Siste 24 timer"
assert names[1] == "Leder"  # AssertionError, second element is Alle pluss-artikler

# to do: page object model design pattern, implement testing different resolutions(desktop, tablet, mobile)
