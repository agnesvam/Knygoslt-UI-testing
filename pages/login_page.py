from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
class Login:
    textbox_email_id= "emailInput"
    textbox_pass_id= "passwordInput"
    btn_login_xpath="/html/body/main/div/div[2]/div[1]/div/div/div/form/div[4]/div/input"
    btn_cookies= "/html/body/div/div[2]/div[2]/a[2]"
    btn_profile= '/html/body/header/div[3]/div[1]/div[4]/div/div[2]/a[1]/span[1]/i'

    logout_linktxt='Atsijung'

    def __init__(self,driver):
        self.driver=driver

    def setEmail(self, email):
        self.driver.find_element(By.ID ,self.textbox_email_id).clear()
        self.driver.find_element(By.ID ,self.textbox_email_id).send_keys(email)

    def setPass(self, password):
        self.driver.find_element(By.ID ,self.textbox_pass_id).clear()
        self.driver.find_element(By.ID ,self.textbox_pass_id).send_keys(password)

    def clickLogin(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH ,self.btn_cookies).click()
        self.driver.find_element(By.XPATH ,self.btn_login_xpath).click()

    def clickProfile(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH ,self.btn_profile).click()
       
      
        

    # def clickLogout(self):
    #     self.driver.find_element_by_link_text(self.logout_linktxt).click()
