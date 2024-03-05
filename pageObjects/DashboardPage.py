import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:
    timesheet_btn = "//span[@class='sidebar_menu_link' and text() = 'Timesheet']"

    def __init__(self, driver):
        self.driver = driver

    def go_to_timesheet_page(self):
        self.driver.find_element(By.XPATH, self.timesheet_btn).click()

    def wait_for_loader(self):
        WebDriverWait(self.driver, 15).until(EC.invisibility_of_element(self.driver.find_element(By.ID, "divLoading")))
