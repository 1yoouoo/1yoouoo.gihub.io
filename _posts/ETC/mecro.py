import pyautogui as pag
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 0. chrome driver 다운로드
pag.hotkey('win', 's')
pag.write('chrome')
time.sleep(0.5)
pag.press('enter')
time.sleep(1)
pag.hotkey('alt', 'space', 'x')
pag.moveTo(300, 52, 1)
time.sleep(0.5)
pag.click()
pag.write('https://chromedriver.chromium.org/downloads')
time.sleep(0.5)
pag.press('enter')
time.sleep(0.5)
pag.moveTo(978, 300, 1)
pag.click()
pag.moveTo(978, 392, 0.2)
pag.click()
time.sleep(0.5)
pag.moveTo(159, 298, 2)
pag.click()
time.sleep(0.5)
pag.moveTo(101, 1013, 2)
pag.click()
time.sleep(0.5)
pag.moveTo(1670, 434, 2)
pag.click()
time.sleep(0.5)
pag.write('chrome')
pag.moveTo(1007, 502, 0.2)
pag.doubleClick()
time.sleep(2)
pag.hotkey('alt', 'F4')
time.sleep(1)
pag.moveTo(1379, 760, 0.2)
pag.click()
pag.hotkey('alt', 'F4')
time.sleep(1)
pag.click()
pag.hotkey('alt', 'F4')
time.sleep(1)



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