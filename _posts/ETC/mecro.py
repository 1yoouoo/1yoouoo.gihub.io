import pyautogui
import time

while True:
    time.sleep(2)
    pyautogui.click()


'''
import pyautogui as pg
import time
import schedule
from multiprocessing import Process
def _456():
    while True:
        qt1 = pg.confirm(title='',text='당신은 이지윤 입니까?')
        if qt1 == 'OK':
            qt2 = pg.password()
            if qt2 == '1008':
                pg.alert('오늘도 열공!')
                break
            else:
                pg.alert('왜 지윤이인 척하십니까? 허허..')
        else:
            pg.alert('죄송하지만 가능하다면 다른 자리 이용해주시겠습니까..                      프로그램 까는데 너무 오래걸립니다 ㅜ')

def click_():
    time.sleep(3)
    pg.click()


p1 = Process(target=_456) 
p2 = Process(target=click_) 

p1.start()
p2.start()
'''