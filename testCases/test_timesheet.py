from pageObjects.LoginPage import LoginPage
from driverfactory.initializeDriver import InitailizeDriver
from utilities.readProperties import ReadConfig
from Configurations.configProperties import CommonData
from utilities.createlog import LogGen
from pageObjects.DashboardPage import DashboardPage
from pageObjects.TimesheetPage import TimesheetPage


class Test_Timesheet:
    def test_add_timesheet(self):
        LogGen.static_logger.info("------ test_add_timesheet started ------------")
        self.lp = LoginPage(self.driver)
        self.lp.go_to_site(CommonData.url)
        self.lp.login_to_app(CommonData.username, CommonData.password)
        dp = DashboardPage(self.driver)
        dp.wait_for_loader()
        dp.wait_for_loader()
        dp.go_to_timesheet_page()
        dp.wait_for_loader()
        dp.wait_for_loader()
        tp = TimesheetPage(self.driver)
        flag = tp.add_timesheet()
        assert flag == True

    def test_add_absence(self):
        LogGen.static_logger.info("------ test_add_timesheet started ------------")
        self.lp = LoginPage(self.driver)
        self.lp.go_to_site(CommonData.url)
        self.lp.login_to_app(CommonData.username, CommonData.password)
        dp = DashboardPage(self.driver)
        dp.wait_for_loader()
        dp.wait_for_loader()
        dp.go_to_timesheet_page()
        dp.wait_for_loader()
        dp.wait_for_loader()
        tp = TimesheetPage(self.driver)
        flag = tp.add_absence()
        assert flag == True
