from selenium.webdriver.common.by import By


class SuccessPage:
    def __init__(self, driver):
        self.driver = driver

    succespage = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def SuccesInfo(self):
        return self.driver.find_element(*SuccessPage.succespage)
