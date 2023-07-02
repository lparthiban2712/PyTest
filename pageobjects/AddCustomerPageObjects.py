from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class AddCustomersObjects:
    menu_customers_xpath="//ul[contains(@class,'side')]/li[4]/a/p"
    menuitems_customers_xpath = " //ul[contains(@class,'side')]/li[4]/ul/li[1]"
    button_Add_New_xpath="//a[normalize-space()='Add new']"
    textbox_email_id="Email"
    textbox_password_id = "Password"
    textbox_firstName_id = "FirstName"
    textbox_lastName_id = "LastName"
    radio_button_male_id="Gender_Male"
    radio_button_female_id = "Gender_Female"
    textbox_dob_id="DateOfBirth"
    textbox_company_name_id="Company"
    checkbox_Tax_Exempted_id="IsTaxExempt"
    textbox_newletterfield_xpath="//ul[@id='SelectedNewsletterSubscriptionStoreIds_taglist']/parent::div"
    list_newsletteroptions_xpath="//ul[@id='SelectedNewsletterSubscriptionStoreIds_listbox']/li"
    textbox_rolesfield_xpath="//ul[@id='SelectedCustomerRoleIds_taglist']/parent::div"
    list_rolesfield_xpath = "//ul[@id='SelectedCustomerRoleIds_listbox']/li"
    listitem_ForumModerator_xpath="//li[text()='Forum Moderators']"
    listitem_Administrators_xpath = "//li[text()='Administrators']"
    listitem_Guests_xpath = "//li[text()='Guests']"
    listitem_Registered_xpath = "//li[text()='Registered']"
    listitem_Vendors_xpath = "//li[text()='Vendors']"
    dropdown_managerofvendor_id="VendorId"
    textbox_Admin_Comment_id="AdminComment"
    button_save_name="save"


    def __init__(self,driver):
        self.driver=driver

    def selectcustomermenu(self):
        self.driver.find_element(By.XPATH,self.menu_customers_xpath).click()
        # wait=WebDriverWait(self.driver,20,poll_frequency=2)
        # wait.until(expected_conditions.element_to_be_clickable(customer))
        # customer.click()

    def selectcustomermenuitem(self):
        self.driver.find_element(By.XPATH,self.menuitems_customers_xpath).click()

    def clickAddNewbutton(self):
        self.driver.find_element(By.XPATH,self.button_Add_New_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.ID,self.textbox_email_id).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)

    def setFirstName(self,fname):
        self.driver.find_element(By.ID,self.textbox_firstName_id).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.ID,self.textbox_lastName_id).send_keys(lname)

    def selectGender(self,gender):
        if gender=='male':
            self.driver.find_element(By.ID,self.radio_button_male_id).click()
        else:
            self.driver.find_element(By.ID, self.radio_button_female_id).click()

    def setDoB(self,dob):
        self.driver.find_element(By.ID,self.textbox_dob_id).send_keys(dob)

    def setCompanyName(self,cname):
        self.driver.find_element(By.ID,self.textbox_company_name_id).send_keys(cname)

    def setTaxExempted(self,text):
        if text=="yes":
            self.driver.find_element(By.ID,self.checkbox_Tax_Exempted_id).click()

    def clickNewletter(self):
        self.driver.find_element(By.XPATH,self.textbox_newletterfield_xpath).click()

    def setNewletter(self,option):
        alloption=self.driver.find_elements(By.XPATH,self.list_newsletteroptions_xpath)
        for options in alloption:
            if options.text==option:
                #options.click()
                self.driver.execute_script("arguments[0].click();",options)
                break

    def clickRoles(self):
        self.driver.find_element(By.XPATH,self.textbox_rolesfield_xpath).click()

    def setRoles(self,setrole):
        if setrole=="Registered":
            self.driver.find_element(By.XPATH,"//span[text()='Registered']//following-sibling::span").click()
            self.driver.find_element(By.XPATH, self.listitem_Registered_xpath).click()
        elif setrole=="Administrators":
            self.driver.find_element(By.XPATH, "//span[text()='Registered']//following-sibling::span").click()
            self.driver.find_element(By.XPATH,self.listitem_Administrators_xpath).click()
        elif setrole=="Guests":
            self.driver.find_element(By.XPATH, "//span[text()='Registered']//following-sibling::span").click()
            self.driver.find_element(By.XPATH,self.listitem_Guests_xpath).click()
        elif setrole=="ForumModerator":
            self.driver.find_element(By.XPATH, "//span[text()='Registered']//following-sibling::span").click()
            self.driver.find_element(By.XPATH,self.listitem_ForumModerator_xpath).click()
        elif setrole=="Vendors":
            #self.driver.find_element(By.XPATH, "//span[text()='Registered']//following-sibling::span").click()
            self.driver.find_element(By.XPATH,self.listitem_Vendors_xpath).click()


    def setManagerofVendor(self,visibletext):
        dropdown=self.driver.find_element(By.ID,self.dropdown_managerofvendor_id)
        option = Select(dropdown)
        option.select_by_visible_text(visibletext)

    def setAdminComments(self,comments):
        self.driver.find_element(By.ID,self.textbox_Admin_Comment_id).send_keys(comments)

    def clickSave(self):
        self.driver.find_element(By.NAME,self.button_save_name).click()


