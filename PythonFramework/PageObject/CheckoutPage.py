from selenium.webdriver.common.by import By


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver


    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    cardbutton = (By.XPATH,"//a[@class='nav-link btn btn-primary']")
    productname = (By.LINK_TEXT,"Blackberry")
    successbutton = (By.XPATH, "//button[@class='btn btn-success']")
    selectIND = (By.ID, "country")
    ClickIND = (By.LINK_TEXT, "India")
    Checkboxclick = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchasebutton = (By.XPATH, "//input[@value='Purchase']")

    def GetCardTitle(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def GetCardButton(self):
        return self.driver.find_element(*CheckOutPage.cardbutton)


    def GetProductName(self):
        return self.driver.find_element(*CheckOutPage.productname)


    def GetSuccessButton(self):
        return self.driver.find_element(*CheckOutPage.successbutton)


    def SelectIndia(self):
        return self.driver.find_element(*CheckOutPage.selectIND)


    def ClickIndia(self):
        return self.driver.find_element(*CheckOutPage.ClickIND)


    def CheckBoxClick(self):
        return self.driver.find_element(*CheckOutPage.Checkboxclick)


    def PurchaseButton(self):
        return self.driver.find_element(*CheckOutPage.purchasebutton)
