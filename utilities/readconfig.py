import configparser
config=configparser.RawConfigParser()
#config.read(".\\configurations\\config.ini")
config.read("C:\\Users\\admin\\PycharmProjects\\SeleniumWithPyTest\\configurations\\config.ini")
class readconfig:
    @staticmethod
    def geturl():
        url=config.get('common info','baseurl')
        return url

    @staticmethod
    def getemail():
        email = config.get('common info', 'email')
        return email

    @staticmethod
    def getpassword():
        password = config.get('common info', 'password')
        return password
