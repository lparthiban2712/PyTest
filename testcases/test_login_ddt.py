import time
from selenium import webdriver
from utilities.readconfig import readconfig
from utilities import xlutilities
from pageobjects.LoginPageObjects import LoginPage
class Test_loginddttest:
    def test_ddt_login(self,setup):
        self.filepath="C:\\Users\\admin\\PycharmProjects\\SeleniumWithPyTest\\testdata\\logintestdata.xlsx"
        maxrows=xlutilities.max_rows(self.filepath,"Sheet1")
        self.driver = setup
        self.baseurl = readconfig.geturl()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        print(maxrows)
        resultlist=[]
        for r in range (2,maxrows+1):
            self.driver.get(self.baseurl)
            uname=xlutilities.read_data(self.filepath,"Sheet1",r,1)
            pwd=xlutilities.read_data(self.filepath,"Sheet1",r,2)
            expResult=xlutilities.read_data(self.filepath,"Sheet1",r,3)
            print(uname," ",pwd," ",expResult)
            lp = LoginPage(self.driver)
            lp.setemail(uname)
            lp.setpassword(pwd)
            lp.clicklogin()
            time.sleep(3)
            actTitle=self.driver.title
            if actTitle=="Dashboard / nopCommerce administration":
                actResult="Pass"
                if expResult==actResult:
                    resultlist.append("Pass")
                    xlutilities.write_data(self.filepath, "Sheet1", r, 4, "Pass")
                    xlutilities.fill_green(self.filepath, "Sheet1", r, 4)
                    lp.clicklogout()
                    #time.sleep(5)
                else:
                    resultlist.append("Fail")
                    xlutilities.write_data(self.filepath, "Sheet1", r, 4, "Fail")
                    xlutilities.fill_red(self.filepath, "Sheet1", r, 4)
            elif actTitle!="Dashboard / nopCommerce administration":
                actResult="Fail"
                if expResult==actResult:
                    resultlist.append("Pass")
                    xlutilities.write_data(self.filepath, "Sheet1", r, 4, "Pass")
                    xlutilities.fill_green(self.filepath, "Sheet1", r, 4)
                else:
                    resultlist.append("Fail")
                    xlutilities.write_data(self.filepath, "Sheet1", r, 4, "Fail")
                    xlutilities.fill_red(self.filepath, "Sheet1", r, 4)
        if "Fail" not in resultlist:
            assert True
            self.driver.close()
        else:
            assert False
            self.driver.close()