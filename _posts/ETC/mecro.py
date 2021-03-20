
# https://www.python.org/  다운로드
# cmd
# pip install pyautogui
# pip install selenium

################################################

import pyautogui as pag
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# gmail.com 최대창 해놓고 시작


# 1. chrome driver 다운로드

time.sleep(1)
pag.moveTo(430, 99, 1)
pag.click()
time.sleep(3)
pag.moveTo(615, 788, 1)
pag.click()
time.sleep(0.5)
pag.press('tab')
time.sleep(0.5)
pag.press('enter')
time.sleep(0.5)
pag.hotkey('alt', 'F4')
time.sleep(1)
pag.moveTo(300, 52, 1)
time.sleep(0.5)
pag.click()
pag.write('https://chromedriver.chromium.org/downloads')
time.sleep(0.5)
pag.press('enter')
time.sleep(0.5)
pag.moveTo(978, 300, 2)
pag.click()
pag.moveTo(977, 412, 0.2)
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
pag.moveTo(1004, 497, 0.2)
pag.click()
pag.hotkey('ctrl', 'c')
pag.doubleClick()
time.sleep(2)
pag.hotkey('alt', 'F4')
time.sleep(1)
pag.moveTo(1182, 432, 1)
pag.click()
time.sleep(1)
pag.write('C:\\Users\\CKIRUser\\AppData\\Local\\Programs\\Python\\Python39')
pag.press('enter')
pag.moveTo(1704, 916, 1)
pag.click()
pag.hotkey('ctrl', 'v')
time.sleep(1)
pag.click()
pag.hotkey('alt', 'F4')
time.sleep(1)
pag.click()
pag.hotkey('alt', 'F4')
time.sleep(1)


# 2. vscode 파일 다운로드

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(3)
driver.get('https://code.visualstudio.com/')
time.sleep(3)
elem = driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/div/div/div[1]/div[2]/div[1]/button[2]").click()
pag.moveTo(424, 1014, 2)
pag.click()


# 3. git desktop 파일 다운로드

time.sleep(1)
driver.get('https:\//desktop.github.com/')
time.sleep(3)
elem = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/a[2]").click()
pag.moveTo(424, 1014, 2)
pag.click()


# 4. git 파일 다운로드

time.sleep(1)
driver.get('https://git-scm.com/')
time.sleep(3)
elem = driver.find_element_by_xpath("/html/body/div[3]/div/div/section[2]/div/a[2]").click()
pag.moveTo(412, 1011, 3)
pag.click()


# 다운로드가 다 될 때까지 바탕화면에서 대기

time.sleep(2)
pag.hotkey('win', 'd')
time.sleep(60)


# 2-(1). vscode 다운로드

time.sleep(1)
pag.hotkey('win', 's')
time.sleep(0.5)
pag.write('C:\\Users\\CKIRUser\\Downloads')
pag.press('enter')
time.sleep(0.5)
pag.hotkey('ctrl', 'f')
pag.write('vscode')
time.sleep(0.5)
pag.press('tab')
time.sleep(0.5)
pag.press('tab')
time.sleep(0.5)
pag.press('space')
time.sleep(0.5)
pag.press('enter')

# 2-(2). 실행

time.sleep(2)
pag.press('Enter')
time.sleep(3)
pag.hotkey('Alt', 'a')
time.sleep(1)
pag.press('enter', presses=5, interval=1)
time.sleep(30)
pag.press('enter')
time.sleep(7)
pag.hotkey('alt', 'space')
time.sleep(1)
pag.press('x')
time.sleep(1)
pag.hotkey('ctrl', 'shift', 'x')
time.sleep(1)
pag.write('python')
pag.moveTo(276, 280, 3)
pag.click()
time.sleep(30)
pag.hotkey('Alt', 'F4')


# 3-(1). git desktop 파일 다운로드

time.sleep(2)
pag.moveTo(1524, 762, 1)
pag.click()
time.sleep(0.5)
pag.hotkey('ctrl', 'f')
pag.write('github')
time.sleep(0.5)
pag.press('tab')
time.sleep(0.5)
pag.press('tab')
time.sleep(0.5)
pag.press('space')
time.sleep(0.5)
pag.press('enter')

# 3-(2). 실행

time.sleep(30)
pag.moveTo(658, 616, 2)
pag.click()
pag.moveTo(887, 440, 2)
pag.click()
pag.write('1yoouoo@gmail.com')
time.sleep(1)
pag.press('tab')
time.sleep(1)
pag.write('Vhdpqj458!')
time.sleep(1)
pag.press('Enter')
pag.moveTo(745, 163, 2)
pag.click()
pag.moveTo(1031, 226, 2)
pag.click()
pag.moveTo(556, 635, 2)
pag.click()
pag.moveTo(547, 626, 2)
pag.click()
pag.moveTo(1069, 484, 2)
pag.click()
pag.moveTo(1165, 779, 2)
pag.click()
pag.moveTo(1003, 643, 2)
pag.click()
time.sleep(10)
pag.moveTo(885, 205, 2)
pag.dragTo(x=0, y=500, duration=2)
pag.hotkey('win', 'd')

# 4-(1). git 다운로드ss

pag.moveTo(124, 1062, 3)
pag.click()
time.sleep(0.5)
pag.hotkey('ctrl', 'f')
pag.write('bit')
time.sleep(0.5)
pag.press('tab')
time.sleep(0.5)
pag.press('tab')
time.sleep(0.5)
pag.press('space')
time.sleep(0.5)
pag.press('enter')

# 4-(2). 실행

pag.moveTo(1075, 689, 2)
pag.click(clicks = 20, interval = 0.5)
time.sleep(40)
pag.press('enter')
time.sleep(3)
pag.hotkey('ctrl', 'w')


# 5. 마무리

# 5-(1). 1yoouoo.github.io
pag.moveTo(620, 50, 2)
pag.click()
time.sleep(1)
pag.write('https://1yoouoo.github.io/')
time.sleep(1)
pag.press('enter')
time.sleep(1)

# 5-(2). github.com
pag.hotkey('ctrl', 't')
time.sleep(1)
pag.write('https://github.com/1yoouoo/1yoouoo.github.io')
pag.press('enter')
time.sleep(1)

# 5-(3). 백준(로그인)
pag.hotkey('ctrl', 't')
time.sleep(1)
pag.write('https://www.acmicpc.net/login?next=%2F')
pag.press('enter')
time.sleep(3)
pag.write('1yoouoo')
time.sleep(1)
pag.press('tab')
time.sleep(1)
pag.write('Vhdpqj458!')
time.sleep(1)
pag.press('tab')
time.sleep(1)
pag.press('space')
time.sleep(1)
pag.press('tab')
time.sleep(1)
pag.press('space')
time.sleep(4)

# 5-(4). python tutor
pag.hotkey('ctrl', 't')
time.sleep(1)
pag.write('http://pythontutor.com/live.html#mode=edit')
pag.press('enter')
time.sleep(1)

# 5-(5). google.com
pag.hotkey('ctrl', 't')
time.sleep(1)
pag.write('google.com')
pag.press('enter')


# 5-(6). youtube.com
pag.hotkey('ctrl', 't')
time.sleep(1)
pag.write('https://www.youtube.com/')
pag.press('enter')



####################################################