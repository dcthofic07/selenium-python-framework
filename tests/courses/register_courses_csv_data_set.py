from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import ResultStatus
import unittest
import pytest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData
from pages.home.navigation_page import NavigationPage


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesCSVDataTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.rcp = RegisterCoursesPage(self.driver)
        self.ts = ResultStatus(self.driver)
        self.np = NavigationPage(self.driver)

    def setUp(self):
        self.np.navigateToAllCourses()

    @pytest.mark.run(order=1)
    @data(*getCSVData("C:\\Users\\dcthofic07\\workspace_python\\automation_framework_1\\testdata.csv"))
    @unpack
    def test_invalid_enrollment(self, courseName, ccNum, ccExp, ccCVV):
        self.rcp.enterCourseName(courseName)
        self.rcp.selectCourseToEnroll()
        self.rcp.fullCourseName(courseName)
        self.rcp.enrollCourse(ccNum, ccExp, ccCVV)
        result = self.rcp.verifyEnrollFailed()
        self.ts.markFinal("test_invalid_enrollment", result, "Enrollment failed verification")
