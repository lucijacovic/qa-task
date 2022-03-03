import pytest
from selenium import webdriver

driver = None


def pytest_addoption(parser):  # cmd: py.test --browser_name chrome --window_size desktop
    parser.addoption("--browser_name", action="store", default="chrome")
    # parser.addoption("--window_size", action="store", default="desktop")


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")  # local path! (change accordingly)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")  # local path!
    elif browser_name == "IE":
        driver = webdriver.Ie(executable_path="C:\\IEDriverServer.exe")  # local path!
    # other possible browsers: safari, microsoft edge, opera etc.
    driver.get("https://finansavisen.no/")

    # window_size = request.config.getoption("--window_size")
    # if window_size == "desktop":
    #   driver.maximize_window()
    #   TestOne(BaseClass).test_newsDesktop (would this work? or separate tests for each resolution?)
    # elif window_size == "tablet":
    #   driver.set_window_size(1366, 768)
    # upon doing some manual checks, tablet resolutions share same class names with desktop resolutions
    #   TestOne(BaseClass).test_newsDesktop (?)
    # elif window_size == "mobile":
    #   driver.set_window_size(360, 640)
    #   TestOne(BaseClass).test_newsMobile (?)

    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

# pasted code for screenshots when tests fail
# commented cause not really needed, hard to tell from screenshots what went wrong in this case

# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     """
#         Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
#         :param item:
#         """
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file_name = report.nodeid.replace("::", "_") + ".png"
#             _capture_screenshot(file_name)
#             if file_name:
#                 html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#
# def _capture_screenshot(name):
#     driver.get_screenshot_as_file(name)
