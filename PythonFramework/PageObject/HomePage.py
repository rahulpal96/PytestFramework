from selenium.webdriver.common.by import By


class Homepage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.LINK_TEXT, "Shop")
    name = (By.XPATH, "//div[@class='container']/form[1]/div[1]/input[1]")
    email = (By.XPATH, "//div[@class='container']/form[1]/div[2]/input[1]")
    password = (By.XPATH, "//div[@class='container']/form[1]/div[3]/input[1]")
    checkbox = (By.XPATH, "//div[@class='container']/form[1]/div[4]/input[1]")
    gender = (By.XPATH, "//div[@class='container']/form[1]/div[5]/select/option[1]")
    Empstatus = (By.XPATH, "//input[@id='inlineRadio2']")
    DOB = (By.XPATH, "//input[@name='bday']")
    submit = (By.XPATH, "//input[@type='submit']")
    Text = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def shopitem(self):
        return self.driver.find_element(*Homepage.shop)


    def GetName(self):
        return self.driver.find_element(*Homepage.name)


    def GetEmail(self):
        return self.driver.find_element(*Homepage.email)


    def GetPassword(self):
        return self.driver.find_element(*Homepage.password)


    def GetCheckBox(self):
        return self.driver.find_element(*Homepage.checkbox)



    def GetGender(self):
        return self.driver.find_element(*Homepage.gender)


    def GetEmpStatus(self):
        return self.driver.find_element(*Homepage.Empstatus)


    def GetDOB(self):
        return self.driver.find_element(*Homepage.DOB)


    def GetSubmit(self):
        return self.driver.find_element(*Homepage.submit)


    def GetText(self):
        return self.driver.find_element(*Homepage.Text)
