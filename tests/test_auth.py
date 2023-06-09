
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import Login
import time
from utilities.read_properties import ReadConfig


class Test_Auth:

    baseURL = ReadConfig.getWebUrl()
    email = ReadConfig.getEmail()
    password= ReadConfig.getPass()
    bademail = ReadConfig.getBadEmail()
    badpassword= ReadConfig.getBadPass()


    def test_homepage(self,setup):
    
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
 
        if act_title == "Prisijungimas - Knygos.lt":
            assert True
            self.driver.close()
            self.driver.quit()
        else:
            self.driver.save_screenshot('.\\screenshots'+'test_homepage.png')
            self.driver.close()
            self.driver.quit()
            assert False


    def test_login(self,setup):
       
        self.driver = setup
        self.driver.get(self.baseURL)
        self.login_page= Login(self.driver)

        self.login_page.setEmail(self.email)
        self.login_page.setPass(self.password)
        self.login_page.clickLogin()
      
        self.login_page.clickProfile()
        time.sleep(5)
    
        act_title= self.driver.find_element(By.XPATH ,"//input[@id='form_user_firstname']").get_attribute("value")
        if act_title == self.password :
            self.driver.quit()
            assert True
        else:
            self.driver.quit()
            assert False

    #login negative case
    def test_invalid_login(self,setup):
           
        self.driver = setup
        self.driver.get(self.baseURL)
        self.login_page= Login(self.driver)

        self.login_page.setEmail(self.bademail)
        self.login_page.setPass(self.badpassword)
        self.login_page.clickLogin()

        time.sleep(5)
    
        invalid_error= self.driver.find_element(By.XPATH,'/html[1]/body[1]/main[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]').text
        if invalid_error == "Klaidingi duomenys." :
            self.driver.quit()
            assert True
        else:
            self.driver.quit()
            assert False
            
    #login negative case
    def test_blank_login(self,setup):
           
        self.driver = setup
        self.driver.get(self.baseURL)
        self.login_page= Login(self.driver)

        self.login_page.setEmail('')
        self.login_page.setPass('')
        self.login_page.clickLogin()

        time.sleep(5)
    
        invalid_error= self.driver.find_element(By.XPATH,'/html[1]/body[1]/main[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]').text
        if invalid_error == "Klaidingi duomenys." :
            self.driver.quit()
            assert True
        else:
            self.driver.quit()
            assert False

                            
        




