import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from testCases.conftest import chrome_driver_init
from webdriver_manager.chrome import ChromeDriverManager
from utilities.customLogger import LogGenclass
from utilities.readProperties import Readconfig
import datetime  #for screenshot directory timestamp
import os        #for make directory and value get for datastring
import warnings  #for terminal warning

class Test_001_Login:
    baseurl = Readconfig.getUrlapp() #"https://admin-demo.nopcommerce.com/"
    username = Readconfig.getUsername() #"admin@yourstore.com"
    password = Readconfig.getPassword() #"admin"

    logger = LogGenclass().loggenmethod()  # method call of class - LogGenclass()

    # Make new Directory everytime in 'TestScreenshots' directory with timestamp
    # And save screenshot in newly generated directory
    path = r'C:\Users\achal\PycharmProjects\pythonproject\TestScreenshots' #'../TestScreenshots/'
    DateString = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    os.chdir(path)
    NewFolder = 'TestDate_' + DateString
    os.makedirs(NewFolder)

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
            self.driver.save_screenshot(self.NewFolder + '/test1_Loginpage.png')
            print("Login Page Title is not as expected\n")
            self.logger.info("******** Test 1: FAILED Login Page title is incorrect ******")
            warnings.warn(UserWarning("**** Test 1 Warning:- AssertError:Login Page Title is incorrect")) #terminal warning
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
            self.driver.close()
        else:
            self.driver.save_screenshot(self.NewFolder + '/test2_Dashboardpage.png')
            print("Dashboard Title is not as expected\n")
            self.logger.info("******** Test 2: FAILED Dashboard Title is incorrect ******")
            warnings.warn(UserWarning("**** Test 2 Warning:- AssertError: DashboardPage Title is incorrect"))  # terminal warning
            self.driver.close()
            assert False




"""
    #old way to store screenshot in 'TestScreenshots'
    ss_homepagetitle = '../TestScreenshots/test_1_LoginPageTitle.png'
    ss_Login = '../TestScreenshots/test_2_DashboardPageTitle.png' 
    
"""