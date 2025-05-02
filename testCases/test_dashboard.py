import pytest
from selenium import webdriver
from PageObjects.LoginPage import Login
from PageObjects.DashboardPage import DashboardPage
import time

class Test_001_Login:
    base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"
    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        time.sleep(2)

        login_page = Login(self.driver)
        login_page.setUsername(self.username)
        login_page.setPassword(self.password)
        login_page.clickLogin()
        time.sleep(3)

        # Assertion: Verify Dashboard/Home page appears
        expected_title = "OrangeHRM"
        actual_title = self.driver.title
        assert actual_title == expected_title


        # Now verify dashboard page loaded
        dashboard_page = DashboardPage(self.driver)
        assert dashboard_page.verifyDashboard() == True, "Dashboard page not loaded"

        self.driver.close()
