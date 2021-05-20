import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.utils import os_type
from datetime import datetime
from pathlib import Path

from Configurations.config import Config

#driver = None

# from Configurations.config import TestData

""""# This will get the value from CLI/hooks that is browser name during run time"""


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="my option: type1 or type2"
    )


""""# The init_driver() method will run before every test class(until yield) after yield i.e driver.close() will run 
after all tests """


@pytest.fixture(scope="function")
def init_driver(request):
    # global driver
    #global driver
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-notifications')
    browser = request.config.getoption("browser")
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=Config.CHROME_PATH, options=options)
    elif browser == "firefox":
        driver = webdriver.Firefox(GeckoDriverManager().install())
    elif browser == "edge":
        driver = webdriver.Edge(EdgeChromiumDriverManager(os_type=os_type()).install())
    request.cls.driver = driver
    # try:
    #     driver.get(TestData.BASE_URL)
    # except Exception as e:
    #     print(e)
    #     pass
    # driver.maximize_window()
    yield
    driver.close()


"""##################### pytest HTML Report ##########################"""

""""# It is hook for Adding Environment info to HTML Report"""


def pytest_configure(config):
    config._metadata['Project Name'] = 'SeleniumMethods'
    config._metadata['Module Name'] = 'All'
    config._metadata['Tester'] = 'Arvind'


""""# It is hook for delete/Modify Environment info to HTML Report"""


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # set custom options only if none are provided from command line
    if not config.option.htmlpath:
        now = datetime.now()
        # create report target dir
        reports_dir = Path('Reports', now.strftime('%Y%m%d'))
        reports_dir.mkdir(parents=True, exist_ok=True)
        # custom report file
        report = reports_dir / f"report_{now.strftime('%H%M')}.html"
        # adjust plugin options
        config.option.htmlpath = report
        config.option.self_contained_html = True
