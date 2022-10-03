import pytest
import sys
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='session')
def path_to_chrome():
    return ChromeDriverManager().install()


@pytest.fixture
def chrome_driver_init(path_to_chrome):
    driver = webdriver.Chrome(executable_path=path_to_chrome)
    driver.get('https://google.com')
    driver.maximize_window()
    yield
    driver.quit()


def test_1(chrome_driver_init):
    pass
    print("\nUser Current Version:-", sys.version)


def test_2(chrome_driver_init):
    pass
