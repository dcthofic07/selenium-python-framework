from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import ResultStatus
import unittest
import pytest
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterMultipleCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.rcp = RegisterCoursesPage(self.driver)
        self.ts = ResultStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(("JavaScript for beginners", "9856 2365 5213 2201", "12 / 20", "562"),
          ("Rest API Automation With Rest Assured", "6856 2395 5213 2201", "12 / 22", "986"))
    @unpack
    def test_invalid_enrollment(self, courseName, ccNum, ccExp, ccCVV):
        self.rcp.enterCourseName(courseName)
        self.rcp.selectCourseToEnroll()
        self.rcp.fullCourseName(courseName)
        self.rcp.enrollCourse(ccNum, ccExp, ccCVV)
        result = self.rcp.verifyEnrollFailed()
        self.ts.markFinal("test_invalid_enrollment", result, "Enrollment failed verification")
        self.driver.find_element_by_xpath("//*[@id='navbar-inverse-collapse']//a[contains(text(),'ALL COURSES')]")\
            .click()
