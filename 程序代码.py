import pyautogui as pag
import time
import win32api,win32gui
import win32con
import os


#定义主执行程序
def main():
    openApp()
    while True:
        if pag.locateOnScreen('C:\\Users\\Administrator\\Desktop\\使用的图片\\学习强国登陆.png'):
            denglu()
            continue
        elif pag.locateOnScreen('C:\\Users\\Administrator\\Desktop\\使用的图片\\学习强国电台.png'):
            move_and_click('C:\\Users\\Administrator\\Desktop\\使用的图片\\学习强国电台.png')
            break
        else:
            print('正在识别是否需要登录…')
            continue
    while True:
        try:
            move_and_click('C:\\Users\\Administrator\\Desktop\\使用的图片\\学习强国听文化.png')
            break
        except:
            continue
    while True:
        if pag.locateOnScreen('C:\\Users\\Administrator\\Desktop\\使用的图片\\听音乐.png'):
            move_and_click('C:\\Users\\Administrator\\Desktop\\使用的图片\\听音乐.png')
            break
        elif pag.locateOnScreen('C:\\Users\\Administrator\\Desktop\\使用的图片\\听音乐2.png'):
            move_and_click('C:\\Users\\Administrator\\Desktop\\使用的图片\\听音乐2.png')
            break
        else:
            print('正在查找听音乐……')
            continue
    time.sleep(2)
    pag.moveRel(0, 750, duration=0.25)
    pag.click()
    time.sleep(2)
    while True:
        try:
            move_and_click('C:\\Users\\Administrator\\Desktop\\使用的图片\\全部播放.png')
            break
        except:
            print('正在等待界面显示…')
            continue
    time.sleep(10)
    pag.moveRel(69,660,duration=0.5)
    pag.click()
    time.sleep(10)
    pag.click()
    n = 0
    while not pag.locateOnScreen('C:\\Users\\Administrator\\Desktop\\使用的图片\\学习强国新闻.png'):
        print('正在查找学习新闻界面…')
        n += 1
        if n > 10:
            pag.click()
            break
        else:
            continue
    move_and_click('C:\\Users\\Administrator\\Desktop\\使用的图片\\学习强国新闻.png')
    time.sleep(2)
    guizhou = 'C:\\Users\\Administrator\\Desktop\\使用的图片\\贵州频道.png'
    while not pag.locateOnScreen(guizhou):
        print('正在等待界面显示…')
    move_and_click(guizhou)
    guizhoupt = 'C:\\Users\\Administrator\\Desktop\\使用的图片\\贵州学习平台.png'
    while not pag.locateOnScreen(guizhoupt):
        print('正在等待界面显示…')
    move_and_click(guizhoupt)
    time.sleep(2)
    pag.moveRel(480,700,duration=1)
    time.sleep(2)
    pag.click()
    time.sleep(2)
    pag.moveRel(-382,-602,duration=0.45)
    pag.click()
    guizhouread()
    while not pag.locateOnScreen('C:\\Users\\Administrator\\Desktop\\使用的图片\\贵州学习平台.png'):
        print('正在等待贵州学习平台的界面显示…')
        continue
    time.sleep(2)
    pag.moveRel(14, 374,duration=0.45)
    time.sleep(2)
    pag.click()
    guizhouread()
    y = 374
    for i in range(3):
        y += 150
        while not pag.locateOnScreen('C:\\Users\\Administrator\\Desktop\\使用的图片\\贵州学习平台.png'):
            print('正在等待贵州频道的界面显示…')
            continue
        pag.moveRel(0,y,duration=0.45)
        pag.click()
        guizhouread()
    while not pag.locateOnScreen('C:\\Users\\Administrator\\Desktop\\使用的图片\\新闻推荐.png'):
        print('正在查找新闻推荐图标…')
    move_and_click('C:\\Users\\Administrator\\Desktop\\使用的图片\\新闻推荐.png')
    while not pag.locateOnScreen('C:\\Users\\Administrator\\Desktop\\使用的图片\\播报.png'):
        print('正在等待界面显示…')
    pag.moveRel(32,649,duration=0.45)
    time.sleep(2)
    pag.click()
    while not pag.locateOnScreen('C:\\Users\\Administrator\\Desktop\\使用的图片\\贵州频道文章显示完毕.png'):
        print('正在等待文章显示…')
    print('文章已经显示完毕！')
    pag.moveRel(434,175,duration=0.45)
    time.sleep(2)
    pag.click()
    while not pag.locateOnScreen('C:\\Users\\Administrator\\Desktop\\使用的图片\\分享到短信.png'):
        print('正在等待分享界面打开…')
    print('分享界面已经打开！')
    move_and_click('C:\\Users\\Administrator\\Desktop\\使用的图片\\分享到短信.png')
    time.sleep(2)
    pag.moveRel(300,214,duration=0.45)
    time.sleep(1)
    pag.click()
    while not pag.locateOnScreen('C:\\Users\\Administrator\\Desktop\\使用的图片\\分享到短信.png'):
        print('正在等待分享界面打开…')
    print('分享界面已经打开！')
    move_and_click('C:\\Users\\Administrator\\Desktop\\使用的图片\\分享到平台.png')
    while not pag.locateOnScreen('C:\\Users\\Administrator\\Desktop\\使用的图片\\分享返回定位标识.png'):
        print('正在等待界面打开…')
    print('界面已经打开！')
    pag.moveRel(-44,-641,duration=0.45)
    time.sleep(1)
    pag.click()
    time.sleep(3)
    pag.moveRel(434,866,duration=0.45)
    time.sleep(1)
    pag.click()




    # time.sleep(3)
    # pag.click()
    # pag.moveRel(134,443,duration=0.45)
    # time.sleep(3)
    # pag.click()
    # while not pag.locateOnScreen('C:\\Users\\Administrator\\Desktop\\使用的图片\\贵州频道文章显示完毕.png'):
    #     print('正在等待文章显示…')
    # print('文章已经显示完毕！')






    # pag.moveRel(-433,-865,duration=0.25)
    # pag.click()
    # time.sleep(3)
    # while not pag.locateOnScreen(diantai):
    #     print('正在等待界面显示…')
    # pag.moveRel(175,436,duration=0.45)
    # time.sleep(3)
    # pag.click()


    # move_and_click('.\\使用的图片\\学习强国返回按钮.png')
    # while not pag.locateOnScreen('.\\使用的图片\\每日金句识别.png'):
    #     time.sleep(3)
    #     continue
    # moveto('.\\使用的图片\\每日金句识别.png')
    # time.sleep(2)
    # pag.moveRel(0,-80,duration=0.25)
    # time.sleep(2)
    # pag.click()
    # while not pag.locateOnScreen(shoucang):
    #     print('正在查找收藏按钮…')
    # move_and_click(shoucang)
    # time.sleep(3)
    # move_and_click('.\\使用的图片\\学习强国返回按钮.png')
    #
    #
    #
    #
    #
    #
    #
    #



#定义一个函数，实现鼠标移动并点击
def move_and_click(area):
    tmp1=pag.locateOnScreen(area)
    x, y=pag.center(tmp1)
    pag.moveTo(x, y,duration=0.35)
    time.sleep(0.5)
    pag.click()


#定义一个函数，实现鼠标的定点移动
def moveto(area):
    tmp1 = pag.locateOnScreen(area)
    x, y = pag.center(tmp1)
    pag.moveTo(x, y, duration=0.35)


#定义一个函数用来打开蓝叠APP软件
def openApp():
    n='C:\\Users\\Administrator\\Desktop\\使用的图片\\蓝叠APP.png'
    n1='C:\\Users\\Administrator\\Desktop\\使用的图片\\蓝叠app是否启动.png'
    if pag.locateOnScreen(n):
        while not pag.locateOnScreen(n1):
            move_and_click(n)
            time.sleep(1.5)
            pag.doubleClick()
            time.sleep(5)
        while True:
            try:
                openxxqg()
                break
            except:
                i=os.system('cls')
                print('正在等在界面启动…')
                time.sleep(5)
                continue
    else:
        chosd=win32api.MessageBox(0, "没有找到桌面的蓝叠图标，请确认安装了蓝叠!\n\n是否继续查找？",
                                  "提醒", win32con.MB_YESNO)
        if chosd == 6:
            openApp()
        else:
            pass


#定义一个函数用来打开学习强国APP
def openxxqg():
    n='C:\\Users\\Administrator\\Desktop\\使用的图片\\学习强国APP.png'
    move_and_click(n)

#定义一个函数，操作学习强国的登陆
def denglu():
    n= 'C:\\Users\\Administrator\\Desktop\\使用的图片\\学习强国登陆.png'
    flag =1
    while flag==1:
        try:
            move_and_click(n)
            pag.write('1986122',0.8)
            time.sleep(0.25)
            pag.press('enter')
            flag=0
        except:
            print('正在等待界面显示…')
            continue

#定义一个函数，实现鼠标的无限次滚动
def mousescroll():
    contentend = '.\\使用的图片\\文章阅读完毕标识.png'
    while not pag.locateOnScreen(contentend):
        time.sleep(5)
        pag.scroll(-200)
    else:
        print('本篇文章阅读完毕！')

#定义一个函数，获取蓝叠APP窗口句柄，并将鼠标放置在窗口中心
def movetocenter():
    hw = win32gui.FindWindow('BS2CHINAUI','BlueStacks App Player')
    if win32gui.IsIconic(hw):
        win32gui.ShowWindow(hw, win32con.SW_SHOWNORMAL)
    win32gui.SetForegroundWindow(hw)
    tmp = win32gui.GetWindowRect(hw)
    x0, y0, x1, y1 = tmp
    x = (x1 - x0) / 2 + x0
    y = (y1 - y0) / 2 + y0
    pag.moveTo(x, y, duration=1)

# 定义一个函数，用来控制贵州频道的文章阅读
def guizhouread():
    while True:
        if pag.locateOnScreen('C:\\Users\\Administrator\\Desktop\\使用的图片\\贵州频道文章显示完毕.png'):
            print('文章已显示,正在等待有效阅读时限（按30秒设置的！）…')
            time.sleep(30)
            move_and_click('C:\\Users\\Administrator\\Desktop\\使用的图片\\贵州频道文章阅读返回.png')
            time.sleep(2)
            pag.click()
            break
        else:
            print('正在等待界面显示…')
            time.sleep(2)
            continue


# movetocenter()

main()


