# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://aravindhanm-osondemand.orangehrm.com/symfony/web/index.php/pim/viewEmployeeList/reset/1")
        driver.find_element_by_id("menu_pim_addEmployee").click()
        driver.get("https://aravindhanm-osondemand.orangehrm.com/symfony/web/index.php/pim/addEmployee")
        driver.find_element_by_id("user_name").clear()
        driver.find_element_by_id("user_name").send_keys("")
        driver.find_element_by_id("user_password").clear()
        driver.find_element_by_id("user_password").send_keys("6x@JfcZD@M3@")
        driver.find_element_by_id("firstName").click()
        driver.find_element_by_id("firstName").clear()
        driver.find_element_by_id("firstName").send_keys("Ramesh")
        driver.find_element_by_id("lastName").click()
        driver.find_element_by_id("lastName").clear()
        driver.find_element_by_id("lastName").send_keys("Murugan")
        driver.find_element_by_id("chkLogin").click()
        driver.find_element_by_id("user_name").click()
        driver.find_element_by_id("user_name").click()
        driver.find_element_by_id("user_name").clear()
        driver.find_element_by_id("user_name").send_keys("admin2")
        driver.find_element_by_id("user_password").click()
        driver.find_element_by_id("user_password").clear()
        driver.find_element_by_id("user_password").send_keys("Ramesh@123")
        driver.find_element_by_id("re_password").click()
        driver.find_element_by_id("re_password").clear()
        driver.find_element_by_id("re_password").send_keys("Ramesh@123")
        driver.find_element_by_id("status").click()
        driver.find_element_by_id("status").click()
        #ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=status | ]]
        driver.find_element_by_id("btnSave").click()
        driver.get("https://aravindhanm-osondemand.orangehrm.com/symfony/web/index.php/pim/viewPersonalDetails/empNumber/8")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
