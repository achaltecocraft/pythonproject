import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from testCases.conftest import setup
from webdriver_manager.chrome import ChromeDriverManager
from utilities.customLogger import LogGenclass
from utilities.readProperties import Readconfig
import time
import datetime  #for screenshot directory timestamp
import os        #for make directory and value get for datastring
import warnings  #for terminal warning
from utilities import XLUtils
from openpyxl import load_workbook
from selenium.webdriver.common.by import By

class Test_Login_DDT_Basic:
    baseurl = Readconfig.getUrlapp() #"https://admin-demo.nopcommerce.com/"
    path = r'C:\Users\Achal Trivedi\PycharmProjects\pythonproject\Testdata\logintestdata.xlsx'


    # "..\\Configuration\\config.ini"  //working
    # '../Configuration/config.ini'  //working
    #username = Readconfig.getUsername() #"admin@yourstore.com"
    #password = Readconfig.getPassword() #"admin"
    logger = LogGenclass().loggenmethod()  # method call of class - LogGenclass()


    def test_Login_DDT(self, setup):

        self.logger.info("******** Test_001_Login_DDT ******")
        self.logger.info("******** Verifying the Login Data Driven test ******")
        print("\nTest_DDT: Verify the Dashboard title")
        self.driver = setup
        self.driver.get(self.baseurl)

        self.row = XLUtils.getRowCount(self.path,'sheet1')
        print("No. of rows in test sheet: ",self.row)
        self.column = XLUtils.getColumCount(self.path, 'sheet1')
        print("No. of Column in test sheet: ", self.column)

        lst_status = []

        for r in range(2, self.row + 1):
            self.user = XLUtils.readData(self.path, 'sheet1',r, 1)
            self.logger.info("*****  Read Username from sheet *****")
            self.password = XLUtils.readData(self.path, 'sheet1', r, 2)
            self.logger.info("*****  Read Password from sheet ******")
            self.exp = XLUtils.readData(self.path, 'sheet1', r, 3)
            self.logger.info("***** Read Expected from sheet ******")

            self.lp = Login(self.driver)
            self.lp.setUserName(self.user)
            print("username from Sheet is:", self.user)
            self.lp.setPassword(self.password)
            print("Password from Sheet is:", self.password)
            time.sleep(3)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            if act_title == "Dashboard / nopCommerce administration":
                if self.exp == "Pass":
                    self.logger.info("*****  PASS: Dashboard title is expected  ***** ")
                    self.lp.clickLogout()
                elif self.exp == "Fail":
                    self.logger.info("*****  FAIL: Dashboard title is expected but status is 'FAIL' ******")
                    #self.driver.save_screenshot(Readconfig.getlogindirectory() + '/DDT.png')
                    self.lp.clickLogout()
            else:
                if self.exp == "Pass":
                    self.logger.info("******** PASS: Login credential and Login Title is not as expected but status is 'PASS' ****** ")
                elif self.exp == "Fail":
                    #self.logger.info("***** FAIL: Login credential and Title is not as expected ,status is 'FAIL'  ***** ")
                    self.driver.save_screenshot(Readconfig.getlogindirectory() + '/Login_DDT.png')






        self.logger.info("***** End of DDT Testing *****")
        self.logger.info("***** Completed test_Login_DDT *****")
        print("\nEnd of Data Driven Testing")
        self.driver.close()



"""
    #old way to store screenshot in 'TestScreenshots'
    ss_homepagetitle = '../TestScreenshots/test_1_LoginPageTitle.png'
    ss_Login = '../TestScreenshots/test_2_DashboardPageTitle.png' 
    
    # Make new Directory everytime in 'TestScreenshots' directory with timestamp
    # And save screenshot in newly generated directory
    path = '../TestScreenshots/'
    DateString = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    os.chdir(path)
    NewFolder = 'TestDate_' + DateString
    os.makedirs(NewFolder)
    
"""