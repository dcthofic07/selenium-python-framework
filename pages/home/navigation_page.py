import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _home = "//*[@id='navbar-inverse-collapse']/ul/li[1]/a"
    _my_courses = "//*[@id='navbar-inverse-collapse']/ul/li[4]/a"
    _all_courses = "//*[@id='navbar-inverse-collapse']/ul/li[2]/a"
    _support = "//*[@id='navbar-inverse-collapse']/ul/li[3]/a"
    _user_settings_icon = "//*[@id='dropdownMenu1']/img"
    _sign_in = "//*[@id='navbar-inverse-collapse']/div/div/a"

    def navigateToAllCourses(self):
        self.elementClick(locator=self._all_courses, locatorType="xpath")

    def navigateToMyCourses(self):
        self.elementClick(locator=self._my_courses, locatorType="xpath")

    def navigateToSupport(self):
        self.elementClick(locator=self._support, locatorType="xpath")

    def signIn(self):
        self.elementClick(locator=self._sign_in, locatorType="xpath")

    def navigateToUserSettings(self):
        userSettingsElement = self.waitForElement(locator=self._user_settings_icon,
                                      locatorType="xpath", pollFrequency=1)
        #self.elementClick(element=userSettingsElement)
        self.elementClick(locator=self._user_settings_icon,
                                      locatorType="xpath")