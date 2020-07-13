from pages.home.login_page import LoginPage
from utilities.teststatus import ResultStatus
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = ResultStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.lp.login("test@email.com", "abcabc")
        result1 = self.lp.verifyLoginTitle()
        self.ts.mark(result1, "Title is incorrect")
        result2 = self.lp.verifyLoginSuccess()
        self.ts.markFinal("test_valid_login", result2, "Login was not successful")


    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.lp.logout()
        self.lp.signIn()
        self.lp.login("test@email.com", "abcabca")
        result = self.lp.verifyLoginFailed()
        assert result == True

