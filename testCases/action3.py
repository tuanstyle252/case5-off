from selenium.webdriver.support.color import Color
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

from pageObjects.LoginPage import Loginpage
import time
from selenium.webdriver.common.by import By
from basetest import BaseTest


class Testaction3(BaseTest):

    def test_action3(self):
        lp = Loginpage(self.driver, self.logger)
        lp.login(self.credentials)
        self.driver.find_element(By.XPATH, "//*[@id='password']/div[1]/div/div[1]/input").send_keys("ah8un1tErop6kINSEsTecOgend468GArs123")
        self.driver.find_element(By.XPATH, "//*[@id='passwordNext']/div/button").click()
        time.sleep(2)

        #show front end'ticket #'
        txt_ticket = self.driver.find_element(By.XPATH, "//*[@class='table tables-v2']//tr//th[2]")
        assert txt_ticket.text, "Ticket #"

        txt_status = self.driver.find_element(By.XPATH, "//*[@id='status']/div[1]/div[1]/div[1]/div[1]")
        if txt_status.text == 'Open':
            # show edit/respond/resolve
            hover = self.driver.find_element(By.XPATH, "//*[@class='table tables-v2']//tbody//tr[2]//td[7]")
            actions = ActionChains(self.driver)
            actions.move_to_element(hover).perform()

            edit = self.driver.find_element(By.XPATH, "//*[@id='gfb_app']/main/div/div/div[2]/table/tbody/tr[2]/td[7]/div/div[2]/div[1]/button")
            assert edit.is_displayed()

            respond = self.driver.find_element(By.XPATH, "//*[@id='gfb_app']/main/div/div/div[2]/table/tbody/tr[2]/td[7]/div/div[2]/div[2]/button")
            assert respond.is_displayed()

            resolve = self.driver.find_element(By.XPATH, "//*[@id='gfb_app']/main/div/div/div[2]/table/tbody/tr[2]/td[7]/div/div[2]/div[3]/button")
            assert resolve.is_displayed()
        elif txt_status == 'Resolve':
            edit = self.driver.find_element(By.XPATH, "//*[@id='gfb_app']/main/div/div/div[2]/table/tbody/tr/td[7]/div/div[2]/div/button")
            assert edit.is_displayed()
        self.driver.quit()
