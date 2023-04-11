class Orange_Locators :
    #Test_case_1
    #Orange HRM username & password Locators with valid credentials
    username_inputbox = 'username'
    password_inputbox = 'password'
    #Login_button XPath
    Login_button = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    

    #Test_case_2
    #Orange HRM username & password Locators with invalid credentials
    username_inputbox1 = 'username'
    password_inputbox2 = 'password'
    #Login_button XPath
    Login_button = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'

    #Test_case_3
    #PIM module Xpath
    pim_module = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'
    #add module Xpath
    add_module = '/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'
    #first name Xpath
    employee_firstname = 'firstName'
    #last name XPath
    employee_lastname = 'lastName'
    #save button Xpath
    save_button = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'

    #Test_case_4
    #PIM module Xpath
    pim_module = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'
    #employee name Xpath
    employee_name = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input'
    #searching for employee PIM page Xpath
    search_button = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]'
    #click button Xpath
    #click_button = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div'
    click_button = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[2]/i'
    #edit button Xpath
    #edit_button = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[2]/i'
    #editing  middle name Xpath
    middle_name = 'middleName'
    #saving edited detials save button Xpath
    esave_button = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button'

    #Test_case_5
    #Deleting employee details using trash button Xpath
    trash_button = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[1]/i'
    #yes,delete button Xpath
    yes_delete = '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]'