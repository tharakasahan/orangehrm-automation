import pytest
from selenium import webdriver
from PageObjects.LoginPage import Login
from PageObjects.DashboardPage import DashboardPage
from PageObjects.LeavePage import LeavePage
import time

class Test_001_Login:
    base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"

    def test_login_leave_logout(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(self.base_url)
        time.sleep(2)

        login_page = Login(driver)
        login_page.setUsername(self.username)
        login_page.setPassword(self.password)
        login_page.clickLogin()
        time.sleep(3)

        dashboard_page = DashboardPage(driver)
        assert dashboard_page.verifyDashboard() == True, "Dashboard page not loaded"

        dashboard_page.clickLeave()
        time.sleep(2)

        leave_page = LeavePage(driver)
        assert leave_page.verifyLeavePage() == True, "Leave page not loaded"

        # 🆕 Perform Logout
        dashboard_page.logout()
        time.sleep(2)

        # 🆕 After logout, you can check if login page is showing again
        login_page_title = "OrangeHRM"
        actual_title = driver.title
        assert actual_title == login_page_title, "Logout failed or not returned to login page"

        driver.close()
