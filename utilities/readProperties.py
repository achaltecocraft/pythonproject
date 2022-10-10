import configparser
import datetime
import os

config = configparser.RawConfigParser()
config.read(r'C:\Users\Achal Trivedi\PycharmProjects\pythonproject\Configuration\config.ini') #'../Configuration/config.ini'



class Readconfig():
    @staticmethod   #static method - beacuse need to access method of class without create object of class
    def getUrlapp():
        url = config.get('common info','baseurl')
        return url

    @staticmethod
    def getUsername():
        usrname = config.get('common info', 'username')
        return usrname

    @staticmethod
    def getPassword():
        passwrd = config.get('common info', 'password')
        return passwrd

    @staticmethod
    def getlogindirectory():
        path = config.get('common info', 'loginpath')
        DateString = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        os.chdir(path)
        loginnewfolder = 'Test_shots_' + DateString
        if not os.path.exists(loginnewfolder):
          os.makedirs(loginnewfolder)
        return loginnewfolder

    @staticmethod
    def getdashboarddirectory():
        path = config.get('common info', 'dashboadpath')
        DateString = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        os.chdir(path)
        dashboardnewfolder = 'Test_shots_' + DateString
        if not os.path.exists(dashboardnewfolder):
          os.makedirs(dashboardnewfolder)
        return dashboardnewfolder



# CONFIG.READ PATH
# "..\\Configuration\\config.ini"  //working
#../Configuration/config.ini  //working
#r'C:\Users\Achal Trivedi\PycharmProjects\pythonproject\Configuration\config.ini' //working


# configparser - class
# Rawconfigparser() - method
# create object as 'config'


# how that we can value
# like page object classmethod
# three staticmethod - directly access by class name without creating object
# create method for every variable

"""
def run():
    config = configparser.ConfigParser()
    config.read('../Configuration/config.ini', encoding='utf8')

    for sections in config.sections():
        print (sections)

if __name__ == '__main__':
    run()
"""

#config.read(os.path.join(os.path.dirname(__file__), 'config', 'config.ini'))

"""
1) import configparser

2) call method 'RawConfigParcer()' of 'configParser' ,create 'config' object
code: config = configparser.RawConfigParser()

3) use config.read() for read config.ini file
code : config.read(".\\Configuration\\config.ini")

4)user object method read() for location on 'config.ini' file
code: config.read()

5)make static method for each variable in class 
code :class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseurl')
        return url

6)import package in 'testcase.py' file for access static methods
( from utilites.readProperties import Readconfig )  

Configuration file parser.

A configuration file consists of sections, lead by a "[section]" header,
and followed by "name: value" entries, with continuations and such in
the style of RFC 822.

Intrinsic defaults can be specified by passing them into the
ConfigParser constructor as a dictionary.

class:

ConfigParser -- responsible for parsing a list of
                    configuration files, and managing the parsed database.      

"""