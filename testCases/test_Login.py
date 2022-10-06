import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from testCases.conftest import chrome_driver_init
from webdriver_manager.chrome import ChromeDriverManager
from utilities.customLogger import LogGenclass
from utilities.readProperties import Readconfig


# driver = chromedriver_autoinstaller.install()
# driver = webdriver.Chrome()
# driver.get("https://www.nopcommerce.com/en/demo")

class Test_001_Login:
    baseurl = Readconfig.getUrlapp() #"https://admin-demo.nopcommerce.com/"
    username = Readconfig.getUsername() #"admin@yourstore.com"
    password = Readconfig.getPassword() #"admin"
    ss_homepagetitle = "..\\TestScreenshots\\" + "test_1_homePageTitle.png"
    ss_Login = ".\\TestScreenshots\\" + "test_2_Login.png"
    logger = LogGenclass().loggenmethod()  # method call of class - LogGenclass()


    def test_homePageTitle(self, chrome_driver_init):

        self.logger.info("******** Test 1: Verify the Login Page title ******")
        self.driver = chrome_driver_init
        self.driver.get(self.baseurl)
        print("\nTest 1: Verify the Login Page title")
        act_title = self.driver.title

        if act_title == "Your store. Login":
            print("Login Page Title is as expected\n")
            self.logger.info("******** Test 1: PASSED Login page title is verified ******")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(self.ss_homepagetitle)
            print("Login Page Title is not as expected\n")
            self.logger.info("******** Test 1: FAILED Login Page title is incorrect ******")
            self.driver.close()
            assert False

    def test_Login(self, chrome_driver_init):

        self.driver = chrome_driver_init
        self.driver.get(self.baseurl)
        self.logger.info("******** Test 2: Verify the Dashboard title ******")
        print("\nTest 2: Verify the Dashboard title")
        self.lp = Login(self.driver)  # create object of 'Login' class
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            print("Dashboard Title is as expected\n")
            self.logger.info("******** Test 2: PASSED Dashboard Title is as expected ******")
        else:
            self.driver.save_screenshot(self.ss_Login)
            print("Dashboard Title is not as expected\n")
            self.logger.info("******** Test 2: FAILED Dashboard Title is incorrect ******")
            assert False
