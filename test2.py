import pyautogui as pag
import time

tm = 0
while not pag.locateOnScreen('.\\使用的图片\\蓝叠APP.png'):
    tm += 1
    time.sleep(2)
    print('第%d次寻找蓝叠启动图标…'%tm)
else:
    x, y = pag.center(pag.locateOnScreen('.\\使用的图片\\蓝叠APP.png'))
    pag.moveTo(x,y,duration=1)