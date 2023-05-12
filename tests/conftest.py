from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import pytest
from selenium import webdriver

@pytest.fixture()
def setup():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    return driver
