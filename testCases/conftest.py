import pytest
# import chromedriver_autoinstaller
from selenium import webdriver
import selenium
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service #impor service for 'service=Service(ChromeDriverManager().install())'


@pytest.fixture
def chrome_driver_init(browser):
   #driver = webdriver.Chrome(ChromeDriverManager().install()) #it gived warning in terminal:- DeprecationWarning: executable_path
   driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
   return driver


def pytest_addoption(parser):
   parser.addoption("--browser")


@pytest.fixture
def browser(request):
   return request.config.getoption("--browser")


"""
Double Fixutres() using for not repeat baseuerl in each testcase (only write test cases in test methods)

@pytest.fixture(scope='session')    // first fixures for install chrome driver and session start
def path_to_chrome():
    return ChromeDriverManager().install()   //return chromedrivermanager().install()

@pytest.fixture
    def chrome_driver_init(self,path_to_chrome):   //call path_to_chrome() function
        self.driver = webdriver.Chrome(executable_path=path_to_chrome) //catch return by 'path_to_chrome' method 
        self.driver.get(self.baseurl)
        print("URL is called in chrome driver _init")
        self.driver.maximize_window()
        yield                           //use for repeat upper code in every test cases
        self.driver.quit()
        print("Driver is Quit! and program run successfully")
        
        
        
    Test Class:-     
    def Test_homePageTitle1(self, chrome_driver_init):
        self.driver = webdriver.Chrome(executable_path=path_to_chrome) //with fixtures in each test
        print("Test 1: Home page title is compared")
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Your store. Login":
            assert True
            print("Login Page Title is as expected")
        else:
            assert False
            print("Login Page Title is not as expected")        
"""
