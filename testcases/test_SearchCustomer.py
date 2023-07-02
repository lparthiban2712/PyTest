import random
import string
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageobjects.LoginPageObjects import LoginPage
from pageobjects.AddCustomerPageObjects import AddCustomersObjects
from utilities.readconfig import readconfig
from pageobjects.SearchCustomerPageObjects import searchcustomerobject


class Test_Search_Customer:
    baseURL=readconfig.geturl()
    username=readconfig.getemail()
    password=readconfig.getpassword()

    @pytest.mark.sanity
    def test_search_customer_By_Email(self,setup):
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
        sc=searchcustomerobject(self.driver)
        sc.searchemail("victoria_victoria@nopCommerce.com")
        sc.clicksearch()
        result=sc.serachresult("victoria_victoria@nopCommerce.com")
        assert True==result