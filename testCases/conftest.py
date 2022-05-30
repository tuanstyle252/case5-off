import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def setup():
    option = Options()
    driver =webdriver.Chrome(chrome_options=option, executable_path="D:\\PycharmProjects\\cas5\\drivers\\chromedriver.exe")
    return driver