from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyperclip
import time
from selenium.webdriver.common.by import By


class MessageReader:

    @staticmethod
    def read_message(url: str):
        driver = Chrome('chromedriver/chromedriver.exe')

        try:
            driver.get(url)
            confirm_button = driver.find_element(By.XPATH, '//*[@id="confirm_button"]')
            ac = ActionChains(driver)
            ac.click(confirm_button).perform()
            text_area = driver.find_element(By.XPATH, '//*[@id="note_contents"]')
            time.sleep(1)
            text_area.send_keys(Keys.CONTROL + 'c')
            time.sleep(1)
            text = pyperclip.paste()
            print(text)
            driver.close()
        except Exception as ex:
            print(ex)
            driver.close()
            text = "Ooops something went wrong..."
        return text
