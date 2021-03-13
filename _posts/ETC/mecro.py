import pyautogui as pag
import time



def image_serching(URL):
    pag.moveTo(1231, 59)
    time.sleep(1)
    pag.click()
    pag.write(URL)
    pag.press('enter')
    while True:
        find_img = pag.locateOnScreen('vscode.png')
        if find_img==None:
            time.sleep(3)
        else:
            break
    center = pag.center(image)
    pag.click(center)

image_serching('https://code.visualstudio.com/')





# pyautogui.press('enter', presses=3, interval=3)