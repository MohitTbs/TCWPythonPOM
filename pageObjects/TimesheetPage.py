import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from utilities import utilfunctions


class TimesheetPage:
    add_timesheet_btn = "add_task_link_two"
    emp_drpdwn = "ddltmpopupEmployeeList"
    start_date = "txtStartDateClock"
    end_date = "txtEndDateClock"
    start_time = "txtstartTimeClock"
    end_time = "txtEndTimeClock"
    save_btn = "btntimesheetpopupSave"
    loc_drpdwn = "ddlLocationClocked"
    job_drpdwn = "ddlJobClocked"
    validation_msg = "jSuccess"

    add_absence_btn_xpath = "//a[@data-target='#Add_timeOff']"
    emp_absence_drp_id = "ddlAbsenceEmployeeList"
    start_absence_date_id = "txtstartdateAbsence"
    end_absence_date_id = "txtenddateAbsence"
    start_absence_time_id = "txtStartTime"
    end_absence_time_id = "txtEndTime"
    location_drpdwn_absence_id = "ddlLocationClockedAbsence"
    job_drpdwn_absence_id = "ddlJobClockedAbsence"
    save_absence_btn_id = "btnabsencepopupSave"

    def __init__(self, driver):
        self.driver = driver

    def add_timesheet(self):
        self.driver.find_element(By.ID, self.add_timesheet_btn).click()
        time.sleep(2)
        sel = Select(self.driver.find_element(By.ID, self.emp_drpdwn))
        sel.select_by_visible_text("Hackshaw")
        start_date_box = self.driver.find_element(By.ID, self.start_date)
        start_date_box.clear()
        start_time_list = utilfunctions.start_time_for_timesheet()
        end_time_list = utilfunctions.end_time_for_timesheet()
        start_date_box.send_keys(start_time_list[0])
        end_date_box = self.driver.find_element(By.ID, self.end_date)
        end_date_box.clear()
        end_date_box.send_keys(end_time_list[0])
        start_time_box = self.driver.find_element(By.ID, self.start_time)
        start_time_box.clear()
        start_time_box.send_keys(start_time_list[1] + ' ' + start_time_list[2])
        end_time_box = self.driver.find_element(By.ID, self.end_time)
        end_time_box.clear()
        end_time_box.send_keys(end_time_list[1] + ' ' + end_time_list[2])
        se11 = Select(self.driver.find_element(By.ID, self.loc_drpdwn))
        se11.select_by_visible_text('India')
        se12 = Select(self.driver.find_element(By.ID, self.job_drpdwn))
        se12.select_by_visible_text('Home')
        save_btn_el = self.driver.find_element(By.ID, self.save_btn)
        save_btn_el.click()
        val_msg = self.driver.find_element(By.ID, self.validation_msg)
        flag = val_msg.is_displayed()
        # webdriver.Chrome().find_element(By.XPATH,"").is_displayed()
        return flag

    def add_absence(self):
        self.driver.find_element(By.XPATH, self.add_absence_btn_xpath).click()
        time.sleep(2)
        sel = Select(self.driver.find_element(By.ID, self.emp_absence_drp_id))
        sel.select_by_visible_text("Hackshaw")
        start_date_box = self.driver.find_element(By.ID, self.start_absence_date_id)
        start_date_box.clear()
        start_time_list = utilfunctions.start_time_for_absence()
        end_time_list = utilfunctions.end_time_for_absence()
        start_date_box.send_keys(start_time_list[0])
        end_date_box = self.driver.find_element(By.ID, self.end_absence_date_id)
        end_date_box.clear()
        end_date_box.send_keys(end_time_list[0])
        start_time_box = self.driver.find_element(By.ID, self.start_absence_time_id)
        start_time_box.clear()
        start_time_box.send_keys(start_time_list[1] + ' ' + start_time_list[2])
        end_time_box = self.driver.find_element(By.ID, self.end_absence_time_id)
        end_time_box.clear()
        end_time_box.send_keys(end_time_list[1] + ' ' + end_time_list[2])
        se11 = Select(self.driver.find_element(By.ID, self.location_drpdwn_absence_id))
        se11.select_by_visible_text('India')
        se12 = Select(self.driver.find_element(By.ID, self.job_drpdwn_absence_id))
        se12.select_by_visible_text('Home')
        save_btn_el = self.driver.find_element(By.ID, self.save_absence_btn_id)
        save_btn_el.click()
        val_msg = self.driver.find_element(By.ID, self.validation_msg)
        flag = val_msg.is_displayed()
        # webdriver.Chrome().find_element(By.XPATH,"").is_displayed()
        return flag

