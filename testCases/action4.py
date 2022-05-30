from selenium.webdriver.support.color import Color
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys

from pageObjects.LoginPage import Loginpage
import time
from utilites.readProperties import ReadConfig
from selenium.webdriver.common.by import By


class Testaction4:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    def test_action4(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//*[@id='lock']/div/div/form/div/div/div/div/div[2]/div[2]/span/div/div/div/div/div/div/div/div/div/div[1]/div/a[1]").click()
        self.driver.find_element(By.XPATH, "//*[@id='identifierId']").send_keys("qa-robot@revinate.com")
        self.driver.find_element(By.XPATH, "//*[@id='identifierNext']/div/button/span").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='password']/div[1]/div/div[1]/input").send_keys("ah8un1tErop6kINSEsTecOgend468GArs123")
        self.driver.find_element(By.XPATH, "//*[@id='passwordNext']/div/button").click()
        time.sleep(4)

        # #tickets
        #check descending
        self.driver.find_element(By.XPATH, "//*[@role='table']//tr/th[2]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@role='table']//tr/th[2]").click()
        time.sleep(1)
        ticket = self.driver.find_elements(By.XPATH, "//*[@role='table']/tbody/tr/td[2]")
        before_sort = []
        for i in ticket:
            before_sort.append(i.text)
        template = before_sort
        after_sort = sorted(template, reverse=True)
        assert before_sort == after_sort

        # #check ascending
        self.driver.find_element(By.XPATH, "//*[@role='table']//tr/th[2]").click()
        time.sleep(3)
        ticket = self.driver.find_elements(By.XPATH, "//*[@role='table']/tbody/tr/td[2]")
        before_sort = []
        for i in ticket:
            before_sort.append(i.text)
        template = before_sort
        after_sort = sorted(template)
        assert before_sort == after_sort

        # ticket title
        # check ascending ticket title
        self.driver.find_element(By.XPATH, "//*[@role='table']//tr/th[3]").click()
        time.sleep(2)
        ticket = self.driver.find_elements(By.XPATH, "//*[@role='table']/tbody/tr/td[3]")
        before_sort = []
        for i in ticket:
            before_sort.append(i.text)

        template = before_sort
        after_sort = sorted(template)

        assert before_sort == after_sort

        # check descending ticket title
        self.driver.find_element(By.XPATH, "//*[@role='table']//tr/th[3]").click()
        time.sleep(2)
        ticket = self.driver.find_elements(By.XPATH, "//*[@role='table']/tbody/tr/td[3]")
        before_sort = []
        for i in ticket:
            before_sort.append(i.text)
        template = before_sort
        after_sort = sorted(template, reverse=True)
        assert before_sort == after_sort

        #submitted on
        # check asscending submitted on
        self.driver.find_element(By.XPATH, "//*[@role='table']//tr/th[4]").click()
        time.sleep(2)
        ticket = self.driver.find_elements(By.XPATH, "//*[@role='table']/tbody/tr/td[4]")
        before_sort = []
        for i in ticket:
            before_sort.append(i.text)
        template = before_sort
        after_sort = sorted(template)
        assert before_sort == after_sort

        # check descending submitted on
        self.driver.find_element(By.XPATH, "//*[@role='table']//tr/th[4]").click()
        time.sleep(2)
        ticket = self.driver.find_elements(By.XPATH, "//*[@role='table']/tbody/tr/td[4]")
        before_sort = []
        for i in ticket:
            before_sort.append(i.text)
        template = before_sort
        after_sort = sorted(template, reverse=True)
        assert before_sort == after_sort

        #status
        self.driver.find_element(By.XPATH, "//*[@id='status']/div[1]/div[1]/div[1]/div[2]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//*[@role='table']//tr/th[6]").click()
        # check ascending status
        ticket = self.driver.find_elements(By.XPATH, "//*[@role='table']/tbody/tr/td[6]/span")
        before_sort = []
        for i in ticket:
            before_sort.append(i.text)
        template = before_sort
        after_sort = sorted(template)
        assert before_sort == after_sort

        # check descending status
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//*[@role='table']//tr/th[6]").click()
        ticket = self.driver.find_elements(By.XPATH, "//*[@role='table']/tbody/tr/td[6]")
        before_sort = []
        for i in ticket:
            before_sort.append(i.text)
        template = before_sort
        after_sort = sorted(template, reverse=True)
        assert before_sort == after_sort

        # last updated
        # check asscending last updated
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@role='table']//tr/th[7]").click()
        time.sleep(2)
        ticket = self.driver.find_elements(By.XPATH, "//*[@role='table']/tbody/tr/td[7]")
        before_sort = []
        for i in ticket:
            before_sort.append(i.text)
        template = before_sort
        after_sort = sorted(template)
        assert before_sort == after_sort

        # check ascending last updated
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@role='table']//tr/th[7]").click()
        time.sleep(2)
        ticket = self.driver.find_elements(By.XPATH, "//*[@role='table']/tbody/tr/td[7]")
        before_sort = []
        for i in ticket:
            before_sort.append(i.text)
        template = before_sort
        after_sort = sorted(template, reverse=True)
        assert before_sort == after_sort

        self.driver.close()



























































