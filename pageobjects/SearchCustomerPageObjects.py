from selenium import webdriver
from selenium.webdriver.common.by import By


class searchcustomerobject:

    textbox_email_id="SearchEmail"
    button_search_id="search-customers"
    table_rows_xpath="//table[@id='customers-grid']//tbody/tr"
    table_email_xpath="//table[@id='customers-grid']//tbody/tr/td[2]"

    def __init__(self,driver):
        self.driver=driver

    def searchemail(self,email):
        self.driver.find_element(By.ID,self.textbox_email_id).send_keys(email)


    def clicksearch(self):
        self.driver.find_element(By.ID,self.button_search_id).click()

    def serachresult(self,email):
        flag=False
        #tablerows=self.driver.find_elements(By.XPATH,self.table_rows_xpath)
        results=self.driver.find_elements(By.XPATH, self.table_email_xpath)
        for result in results:
            if result.text==email:
                flag=True
                break
        return flag
