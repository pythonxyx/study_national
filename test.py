import pyautogui as pag
import time

def move_and_click(area):
    tmp1=pag.locateOnScreen(area)
    x,y=pag.center(tmp1)
    pag.moveTo(x,y,duration=0.35)
    time.sleep(0.5)
    pag.click()

# move_and_click('.\\使用的图片\\学习强国登陆.png')
# pag.moveTo(pag.center(pag.locateOnScreen('.\\使用的图片\\播报.png')))
# time.sleep(5)
# pag.moveRel(-400,-750,duration=0.25)

# # time.sleep(5)
print(pag.locateOnScreen('.\\使用的图片\\学习强国电台.png'))
# n=pag.locateOnScreen('.\\使用的图片\\贵州频道文章显示完毕.png')
# if n:
#     print('真')
# elif not n:
#     print('假')
# else:
#     print('None')

# pag.click()
# pag.scroll(-100)

# def xunhuan(n):
#     flag = 1
#     while flag == 1:
#         try:
#             n
#             flag = 0
#         except:
#             continue
#
# def test():
#     print('测试')
# xunhuan(test())

#
# time.sleep(5)
# pag.scroll(-200)

# n=pag.locateAllOnScreen('C:\\Users\\Administrator\\Desktop\\播报.png')
# for i in n:
#     print(i)