from allure_commons.types import AttachmentType
from selenium import webdriver
import allure
import pytest


# severity of test method can be added at classs level or method level . Severity level are minor, normal, critic and blocker
@allure.severity(allure.severity_level.NORMAL)
class TestHRM:

    @allure.severity(allure.severity_level.MINOR)
    def test_Logo(self):
        self.driver = webdriver.Chrome(
            executable_path="C:\\Users\\prana\\OneDrive\\Desktop\\Pranay\\Projects\\Python -Coding\\NopCommerceApp\\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        status = self.driver.find_element_by_xpath("//*[@id='divLogo']/img").is_displayed()
        if status == True:
            assert True
        else:
            assert False
        self.driver.close()

    def test_listemployee(self):
        pytest.skip("Skipping the testcase will script it later")

    @allure.severity(allure.severity_level.BLOCKER)
    def test_login(self):
        self.driver = webdriver.Chrome(
            executable_path="C:\\Users\\prana\\OneDrive\\Desktop\\Pranay\\Projects\\Python -Coding\\NopCommerceApp\\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        actualTitle = self.driver.title
        if (actualTitle == "OrangeHRM123"):
            self.driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_login_screen",
                          attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False
