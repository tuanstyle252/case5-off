from selenium.webdriver.support.color import Color
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
import pytest
import time
import datetime
from selenium.webdriver.common.by import By
from basetest import BaseTest
from pageObjects.LoginPage import Loginpage


class Testaction2(BaseTest):

    def test_action2(self):
        lp = Loginpage(self.driver, self.logger)
        lp.login(self.credentials)

        total = self.driver.find_element(By.XPATH, "//*[@id='gfb_app']/main/div/div/div[2]/p")
        try:
            assert total.is_displayed()
            self.logger.info(f'Passed when validate for the # shown on the top left')
        except Exception as ex:
            self.logger.error(f'Failed when validate for the # shown on the top left '+ str(ex))

        text_title = self.driver.find_elements(By.XPATH, "//*[@class='table tables-v2']//tr/th")
        ar = []
        for i in text_title:
            ar.append(i.text)
        try:
            assert 'TICKET #' and 'TICKET TITLE' and 'SUBMITTED ON' and "ASSIGNEE" and 'ASSIGNEE' and 'LAST UPDATED' in i.text
            self.logger.info(f'Passed when validate for text title TICKET # , TICKET TITLE .. ')
        except Exception as ex:
            self.logger.error(f'Passed when validate for text title TICKET # , TICKET TITLE .. ' +str(ex))

        ticket = self.driver.find_elements(By.XPATH, "//*[@class='table tables-v2']//tbody//tr//td[2]")
        for i in ticket:
            if i.text.isnumeric():
                assert True
            else:
                raise ValueError("column have word")

        ticket_title = self.driver.find_elements(By.XPATH, "//*[@class='table tables-v2']//tbody//tr//td[3]")
        try:
            for i in ticket_title:
                assert i.is_displayed()
                self.logger.info(f'Passed when validate ticket title shown')
                break
        except Exception as ex:
            self.logger.error(f'Failed when validate ticket title shown '+ str(ex))


        #check property column
        time.sleep(2)
        click_ = self.driver.find_element(By.XPATH, "//*[@id='gfb-property-selector']/a")
        ActionChains(self.driver).move_to_element(click_).perform()
        time.sleep(3)
        gjp = self.driver.find_elements(By.XPATH, "//*[@class='sc-hKMtZM dpbvJz dropdown-menu']/a")
        for i in gjp:
            if i.text == "GJP Hotels & Resorts":
                i.click()
                break
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='nav-tabs-tickets']"))).click()

        list_property = self.driver.find_element(By.XPATH, "//*[@id='property']/div/div[1]")
        actions = ActionChains(self.driver)
        actions.move_to_element(list_property).click().send_keys("Yak Hotel Natal").send_keys(Keys.ENTER).perform()

        property = self.driver.find_elements(By.XPATH, "//*[@class='table tables-v2']//tbody//tr//td[4]")
        try:
            for i in property:
                assert i.text == list_property.text
                self.logger.info(f'Passed when validate property column:it shows them name of the property')
                break
        except Exception as ex:
            self.logger.error(f'Failed when validate property column:it shows them name of the property '+ str(ex))

        time.sleep(2)
        #check format datetime
        date = self.driver.find_element(By.XPATH, "//*[@class='table tables-v2']/tbody/tr/td[5]").text
        date_format = '%b %d, %Y'
        try:
            datetime.datetime.strptime(date, date_format)
            self.logger.info(f'Passed when validate data format, MM DD, YYYY')
        except Exception as ex:
            self.logger.error(f'Failed when validate data format, MM DD, YYYY '+ str(ex))

        #check assignee column
        assign_to = self.driver.find_elements(By.XPATH, "//*[@class='table tables-v2']//tbody//tr//td[6]")
        assign_user = self.driver.find_element(By.XPATH, "//*[@id='assignedTo']/div[1]/div[1]/div[1]/div[1]").text
        try:
            for i in assign_to:
                assert i.text == assign_user
                self.logger.info(f'Passed when validate for the assignee column: the user that the ticket was assigned to')
                break
        except Exception as ex:
            self.logger.error(f'Passed when validate for the assignee column: the user that the ticket was assigned to')

        #check status column
        txt_status = self.driver.find_element(By.XPATH, "//*[@class='table tables-v2']//tbody//tr//td[7]")
        try:
            assert txt_status.text == 'OPEN' or txt_status.text == 'RESOLVE'
            self.logger.info(f'Passed when validate for the status column: it shows the status of open or resolved')
        except Exception as ex:
            raise ValueError(f'Failed when validate for the status column: it shows the status of open or resolved ' +str(ex))

        #last update column
        date_update = self.driver.find_elements(By.XPATH, "//*[@class='table tables-v2']//tbody//tr//td[8]//*[@class='ActionsWrapper-sc-17dvs0l hbNKwz']//*[@class='HideOnRowHover-sc-1j5bzee eOVinw hide-on-row-hover']//*[@class='mb-2']")
        for i in date_update:
            txt_date = i.text
            date_format = '%b %d, %Y'
            try:
                datetime.datetime.strptime(txt_date, date_format)
                self.logger.info(f'Passed when validate data format, MM DD, YYYY')
                break
            except Exception as ex:
                self.logger.error(f'Failed when validate data format, MM DD, YYYY ' + str(ex))

        assign_user = self.driver.find_element(By.XPATH, "//*[@id='assignedTo']/div[1]/div[1]/div[1]/div[1]")
        user = self.driver.find_elements(By.XPATH, "//*[@class='table tables-v2']//tbody//tr//td[8]//*[@class='ActionsWrapper-sc-17dvs0l hbNKwz']//*[@class='HideOnRowHover-sc-1j5bzee eOVinw hide-on-row-hover']//*[@class='LastUpdateBy-sc-gjabym TkBrQ']")
        try:
            for i in user:
                assert assign_user.text in i.text
                self.logger.info(f'Passed when validate for the second line:show the last user who updated the ticket')
                break
        except Exception as ex:
            self.logger.error(f'Failed when validate for the second line:show the last user who updated the ticket '+ str(ex))

