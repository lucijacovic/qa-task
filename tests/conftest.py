import pytest
from selenium import webdriver

driver = None

def pytest_addoption(parser): # cmd: py.test --browser_name firefox
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
    elif browser_name == "IE":
        driver = webdriver.Ie(executable_path="C:\\IEDriverServer.exe")
    driver.get("https://finansavisen.no/")
    # window_size = request.config.getoption("--window_size")
    # if window_size == "desktop":
    #   driver.maximize_window()
    # elif window_size == "mobile":
    #   driver.set_window_size(360, 640) #ali kako ce test znat? poseban test, poseban HomePage?
    driver.maximize_window() # insert options for different window sizes, same as for browser
    request.cls.driver = driver
    # driver.set_window_size(360, 640)
    yield
    driver.close()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)