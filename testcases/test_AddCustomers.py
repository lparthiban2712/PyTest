import random
import string
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageobjects.LoginPageObjects import LoginPage
from pageobjects.AddCustomerPageObjects import AddCustomersObjects
from utilities.readconfig import readconfig


class Test_Add_Customer:
    baseURL=readconfig.geturl()
    username=readconfig.getemail()
    password=readconfig.getpassword()

    @pytest.mark.regression
    def test_add_customer(self,setup):
        self.driver=setup
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        #self.driver=webdriver.Firefox()

        self.driver.get(self.baseURL)
        lp=LoginPage(self.driver)
        lp.setemail(self.username)
        lp.setpassword(self.password)
        lp.clicklogin()
        ac=AddCustomersObjects(self.driver)
        ac.selectcustomermenu()
        ac.selectcustomermenuitem()
        ac.clickAddNewbutton()
        ac.setEmail(randomemailgenerator()+"@gmail.com")
        ac.setPassword("sdfgfdg")
        ac.setFirstName("ABCD")
        ac.setLastName("EFGH")
        ac.selectGender("male")
        ac.setDoB("05/17/2021")
        ac.setCompanyName("Kekaraon")
        ac.setTaxExempted("yes")
        ac.clickNewletter()
        ac.setNewletter("Test store 2")
        ac.clickRoles()
        ac.setRoles("Vendors")
        ac.setManagerofVendor("Vendor 2")
        ac.setAdminComments("Jolly")
        ac.clickSave()
        message=self.driver.find_element(By.XPATH,"//div[contains(@class,'alert')]").text
        if "The new customer has been added successfully." in message:
            assert True
            self.driver.close()
        else:
            assert False
            self.driver.close()



def randomemailgenerator(size=8,chars=string.ascii_lowercase+string.digits):
        return ''.join(random.choice(chars) for x in range(size))
