from PageObject.CheckoutPage import CheckOutPage
from PageObject.ConfirmPage import SuccessPage
from PageObject.HomePage import Homepage
from utilities.Baseclass import baseclass


class Testone(baseclass):
    def test_e2e(self):
        log = self.getLogger()
        homepage = Homepage(self.driver)
        homepage.shopitem().click()
        checkotpage = CheckOutPage(self.driver)
        log.info("getting the all cart titles")
        products = checkotpage.GetCardTitle()
        for product in products:
            productname = product.find_element_by_xpath("div/h4/a").text
            if productname == "Blackberry":
                # add item into card
                product.find_element_by_xpath("div/button").click()
        checkotpage.GetCardButton().click()
        productbalck = checkotpage.GetProductName().text
        assert productbalck == productname
        checkotpage.GetSuccessButton().click()
        log.info("Enter the Country name")
        checkotpage.SelectIndia().send_keys("ind")
        self.VerifyLinkPresence("India")
        checkotpage.ClickIndia().click()
        checkotpage.CheckBoxClick().click()
        checkotpage.PurchaseButton().click()
        successinfo = SuccessPage(self.driver)
        log.info("Succes message is printed")
        print(successinfo.SuccesInfo().text)
        self.driver.get_screenshot_as_file("screen.png")