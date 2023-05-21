import configparser

config=configparser.RawConfigParser()
config.read('.\\configurations\\config.ini')

class ReadConfig():
    @staticmethod #to access def w/o creating class obj
    def getWebUrl():
        url=config.get('common information', 'baseURL')
        return url

    @staticmethod
    def getEmail():
        email= config.get('common information', 'email')
        return email
    
    @staticmethod
    def getBadEmail():
        email= config.get('common information', 'bademail')
        return email

    @staticmethod
    def getPass():
        password= config.get('common information', 'password')
        return password
    

    @staticmethod
    def getBadPass():
        password= config.get('common information', 'badpassword')
        return password