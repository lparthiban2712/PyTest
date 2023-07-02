from selenium import webdriver
from selenium.webdriver.common.by import By
from pageobjects.LoginPageObjects import LoginPage
from utilities.readconfig import readconfig
from utilities.customlogger import logger
import  logging

class Test_001_Login:
    url=readconfig.geturl()
    email=readconfig.getemail()
    password=readconfig.getpassword()
    mylog=logger.setlogger()
    def test_hometitle(self,setup):
        self.mylog.info("test_hometitle is started")
        self.driver=setup
        self.driver.get(self.url)
        if self.driver.title=="Your store. Login":
            assert True
            self.driver.close()
            self.mylog.info("test_hometitle is completed")
        else:
            self.driver.save_screenshot(".\\screenshots"+"\\test_hometitle.png")
            self.driver.close()
            assert False
            self.mylog.info("test_hometitle is completed")

    def test_login_valid_credential(self,setup):
            #self.mylog.info("test_login_valid_credential is started")
            self.driver = setup
            self.driver.get(self.url)
            lp = LoginPage(self.driver)
            lp.setemail(self.email)
            lp.setpassword(self.password)
            lp.clicklogin()
            if self.driver.title == "Dashboard / nopCommerce administration":
                assert True
                self.driver.close()
                self.mylog.info("test_login_valid_credential is completed")
            else:
                self.driver.save_screenshot(".\\screenshots"+"\\test_login_valid_credential.png")
                self.driver.close()
                assert False
                self.mylog.info("test_login_valid_credential is completed")