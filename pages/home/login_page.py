import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from pages.home.navigation_page import NavigationPage


class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.np = NavigationPage(driver)

    # Locators
    _login_link = "//*[@id='masthead']/div/div/div/div/div/div[4]/a/div"
    _email_field = "email"
    _password_field = "password"
    _login_btn = "//*[@id='page']//input[@value='Login']"

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="xpath")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginBtn(self):
        self.elementClick(self._login_btn, locatorType="xpath")

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginBtn()

    def verifyLoginSuccess(self):
        result = self.isElementPresent("//*[@id='dropdownMenu1']/img", locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//*[@id='page']//span[contains(text(),'Your username or password is invalid')]"
                                       , locatorType="xpath")
        return result

    def clearFields(self):
        emailField = self.getElement(self._email_field)
        emailField.clear()
        passwordField = self.getElement(self._password_field)
        passwordField.clear()

    def verifyLoginTitle(self):
        return self.verifyPageTitle("All Courses")

    def logout(self):
        self.np.navigateToUserSettings()
        self.elementClick(locator="//*[@id='navbar-inverse-collapse']/div[1]/div/div/ul/li[3]/a",
                          locatorType="xpath")

    def signIn(self):
        self.np.signIn()
