import pyautogui as pag
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 0. chrome driver 다운로드
pag.hotkey('windows', 's')
pag.write('chrome')
pag.press('enter')
pag.hotkey('alt', 'space', 'x')
pag.moveTo(1280, 67)
pag.click()
pag.press('https://chromedriver.chromium.org/downloads')
pag.press('enter')

# 1. vscode 다운로드
driver = webdriver.Chrome()
driver.get("https://code.visualstudio.com/")
elem = driver.find_element_by_css_selector(".link-button dlink").click()
pag.moveTo(1093, 1015)
pag.click()
time.sleep(1)
pag.press('enter')


# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()





# pyautogui.press('enter', presses=3, interval=3)