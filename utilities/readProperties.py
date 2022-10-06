import configparser

config = configparser.RawConfigParser()
config.read("..\\Configuration\\config.ini")

class Readconfig():
    @staticmethod   #static method - beacuse need to access method of class without create object of class
    def getUrlapp():
        url = config.get('common info','baseurl')
        return url

    @staticmethod  # static method - beacuse need to access method of class without create object of class
    def getUsername():
        usrname = config.get('common info', 'username')
        return usrname

    @staticmethod  # static method - beacuse need to access method of class without create object of class
    def getPassword():
        passwrd = config.get('common info', 'password')
        return passwrd







"""
def run():
    config = configparser.ConfigParser()
    config.read('../Configuration/config.ini', encoding='utf8')

    for sections in config.sections():
        print (sections)

if __name__ == '__main__':
    run()
"""



#config = configparser.RawConfigParser()
#config.Read(r'C:\Users\Achal Trivedi\PycharmProjects\pythonproject\Configuration\config.ini')






"""
    @staticmethod
    def getUsername():
        uname = config.get('common info', 'username')
        return uname

    @staticmethod
    def getPassword():
        pwd = config.get('common info', 'password')
        return pwd

"""
# CONFIG.READ PATH TESTING
# "..\\Configuration\\config.ini"  //working
#../Configuration/config.ini
# "../Configuration/config.ini"
#configFilePath = r'E:\Python\configfile\test.txt'