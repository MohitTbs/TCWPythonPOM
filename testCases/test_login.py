from pageObjects.LoginPage import LoginPage
from driverfactory.initializeDriver import InitailizeDriver
from utilities.readProperties import ReadConfig
from Configurations.configProperties import CommonData
from utilities.createlog import LogGen


class Test_Login:
    # user = ReadConfig.getUserName()

    def test_homePageTitle(self):
        # self.lp = LoginPage(InitailizeDriver.driver)
        self.lp = LoginPage(self.driver)
        self.lp.go_to_site(CommonData.url)
        self.lp.login_to_app(CommonData.username, CommonData.password)
