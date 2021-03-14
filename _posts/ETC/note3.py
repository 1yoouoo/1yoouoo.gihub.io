import pyautogui as pag
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys




# 1. vscode 다운로드
driver = webdriver.Chrome()
driver.get("https://code.visualstudio.com/")
elem = driver.find_element_by_css_selector(".link-button dlink").click()
pag.moveTo(1093, 1015)
pag.click()
time.sleep(1)
pag.press('enter')