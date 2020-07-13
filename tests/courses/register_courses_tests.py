from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import ResultStatus
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.rcp = RegisterCoursesPage(self.driver)
        self.ts = ResultStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalid_enrollment(self):
        self.rcp.enterCourseName("Javascript")
        self.rcp.enrollCourse("9856 2365 5213 2201", "12 / 20", "562")
        result = self.rcp.verifyEnrollFailed()
        self.ts.markFinal("test_invalid_enrollment", result, "Enrollment failed verification")

