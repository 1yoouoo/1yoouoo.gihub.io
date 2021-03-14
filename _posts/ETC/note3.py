import pyautogui as pag
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys




# 1. vscode 다운로드
pag.hotkey('win', 's')
pag.write('chrome')
time.sleep(0.5)
pag.press('enter')
time.sleep(1)
pag.hotkey('alt', 'space', 'x')
pag.moveTo(300, 52, 1)
time.sleep(0.5)
pag.click()
pag.write('https://code.visualstudio.com/')
time.sleep(0.5)
pag.press('enter')
pag.moveTo(540, 434, 1)
time.sleep(3)
pag.click()
pag.moveTo(104, 1013, 1)
time.sleep(60)
pag.click()
time.sleep(5)
pag.press('enter')
time.sleep(5)
pag.hotkey('Alt', 'a')
time.sleep(1)
pag.press('enter', presses=5, interval=2)
time.sleep(10)
pag.press('enter')
time.sleep(5)
pag.hotkey('Alt', 'F4')
time.sleep(3)
pag.hotkey('ctrl', 'w')



