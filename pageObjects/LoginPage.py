import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    username_box = "UserName"
    password_box = "Password"
    login_btn = "//button[@value='LogIn']"

    def __init__(self, driver):
        self.driver = driver

    def go_to_site(self, url):
        self.driver.get(url)

    def login_to_app(self, username, password):
        self.driver.find_element(By.ID, self.username_box).send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.ID, self.password_box).send_keys(password)
        self.driver.find_element(By.XPATH, self.login_btn).click()
