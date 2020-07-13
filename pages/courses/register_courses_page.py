from base.basepage import BasePage
import time
import utilities.custom_logger as cl
import logging


class RegisterCoursesPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators:

    _search_box = "//input[@id='search']"
    _search_button = "//*[@id='search']//i"
    _select_course = "//*[@id='course-list']/div/div/a/div[1]/div[1]/img"
    _full_course_name = "//*[@id='zen_cs_desc_with_promo_dynamic']//h1"
    _enroll_button = "//*[@id='zen_cs_desc_with_promo_dynamic']//button"
    _cc_num = "//*[@id='root']/form/span[2]/div/div[2]/span/input"
    _cc_exp = "//*[@id='root']/form/span[2]/span/input"
    _cc_cvv = "//*[@id='root']/form/span[2]/span/input"
    _submit_enroll = "//*[@id='checkout-form']/div/div[3]/div/div[1]/div[2]/div/button[1]"
    _enroll_error_message = "//*[@id='checkout-form']//span[contains(text(),'Your card number is invalid.')]"

    def enterCourseName(self, name):
        self.sendKeys(name, locator=self._search_box, locatorType="xpath")

    def selectCourseToEnroll(self):
        self.elementClick(locator=self._search_button, locatorType="xpath")
        time.sleep(2)
        self.elementClick(locator=self._select_course, locatorType="xpath")

    def fullCourseName(self, name):
        result = self.getText(locator=self._full_course_name, locatorType="xpath")
        if name == result:
            self.enrollInCourse()
        else:
            self.log.error("DID NOT FIND COURSE")

    def enrollInCourse(self):
        self.elementClick(self._enroll_button, locatorType="xpath")

    def enterCardNum(self, num):
        self.switchToFrame("__privateStripeFrame5")
        self.sendKeys(num, self._cc_num, locatorType="xpath")
        self.switchToDefault()

    def enterCardExp(self, exp):
        self.switchToFrame("__privateStripeFrame7")
        self.sendKeys(exp, self._cc_exp, locatorType="xpath")
        self.switchToDefault()

    def enterCardCVV(self, cvv):
        self.switchToFrame("__privateStripeFrame6")
        self.sendKeys(cvv, self._cc_cvv, locatorType="xpath")
        self.switchToDefault()

    def enterCreditCardInformation(self, num, exp, cvv):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)

    def enrollCourse(self, num="", exp="", cvv=""):
        self.webScroll(direction="down")
        self.enterCreditCardInformation(num, exp, cvv)

    def verifyEnrollFailed(self):
        result = self.isElementDisplayed(self._enroll_error_message, locatorType="xpath")
        return result











