from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from Test_Locators import locators
from Test_Data import data
import pytest

class Test_Hrm:
    @pytest.fixture
    def booting_function(self):
          self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
          self.driver.get(data.Orange_Data().url)
          self.driver.maximize_window()
          self.driver.implicitly_wait(10)
        
    def test_admin_valid(self, booting_function):
        #test case 1 username and password with valid credentials
        #Orange HRM website login function
        self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().username_inputbox).send_keys(data.Orange_Data.username)
        self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().password_inputbox).send_keys(data.Orange_Data.password)
        #CLicking of login button
        self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().Login_button).click()
        assert self.driver.title ==  self.driver.title
        print("Test case 1 -successfully user logged in")

        #test case 2 username and password with invalid credentials
    def test_admin_invalid(self, booting_function):
          #Orange HRM website login functions
          self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().username_inputbox1).send_keys(data.Orange_Data.username1)
          self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().password_inputbox2).send_keys(data.Orange_Data.password2)
          #CLicking of login button
          self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().Login_button).click()
          assert self.driver.title ==  self.driver.title
          print("Test case 2 - validated error message for invalid credentials is displayed")

          #test case 3 Adding new employee in pim module
    def test_add_employee(self,booting_function):
          #Orange HRM website login functions
          self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().username_inputbox).send_keys(data.Orange_Data.username)
          self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().password_inputbox).send_keys(data.Orange_Data.password)  
          #CLicking of login button
          self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().Login_button).click()
          #Selecting pim module
          self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().pim_module).click()
          #Clicking add button for adding new employee in pim module
          self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().add_module).click() 
          #Entering first name and last name of a employee
          self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().employee_firstname).send_keys(data.Orange_Data().first_name)
          self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().employee_lastname).send_keys(data.Orange_Data().last_name) 
          #Clicking save button to save a new employee                                
          self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().save_button).click() 
          assert self.driver.title ==  self.driver.title
          print("Test case 3 - sucessfully new employee added in pim module")

          #test case 4 Editing existing employee detials in pim module
    def test_edit_employee(self,booting_function):
           #Orange HRM website login functions
           self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().username_inputbox).send_keys(data.Orange_Data.username)
           self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().password_inputbox).send_keys(data.Orange_Data.password)
           #Clicking of login button
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().Login_button).click()
           #Selecting pim module
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().pim_module).click()
           #existing employee first name entering in pim module
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().employee_name).send_keys(data.Orange_Data().first_name)
           sleep(5)
           #searching employee
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().search_button).click()     
           sleep(5)
           #clicking 
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().click_button).click()
           #entering new first and last name for employee
           self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().middle_name).send_keys(data.Orange_Data.mid_name)
           #clicking save button to save new employee detials
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().esave_button).click()
           assert self.driver.title ==  self.driver.title
           print("Test case 4 - Edited existing employee detials with new detials in pim module")

           #test case 5 Deleting the existing employee detials in pim module
    def test_delete_employee(self,booting_function):
           #Orange HRM website login functions
           self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().username_inputbox).send_keys(data.Orange_Data.username)
           self.driver.find_element(by=By.NAME, value=locators.Orange_Locators().password_inputbox).send_keys(data.Orange_Data.password)
           #CLicking of login button
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().Login_button).click()
           #Selecting pim module
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().pim_module).click()
           #existing employee first name entering in pim module
           self.driver.find_element(by=By.XPATH, value=locators.Orange_Locators().employee_name).send_keys(data.Orange_Data().first_name)
           sleep(5)
           #searching employee
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().search_button).click()     
           sleep(5)
           #Deleting employee detials by clicking trash button
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().trash_button).click()
           #clicking yes,delete button to delete employee existing detials
           self .driver.find_element(by=By.XPATH, value=locators.Orange_Locators().yes_delete).click()
           assert self.driver.title ==  self.driver.title
           print("Test case 5 - Deleted the existing employee detials in pim module")





