import pyautogui as pag
import time
import win32api,win32gui
import win32con


#定义主执行程序
def main():
    # openApp()
    # diantai = '.\\使用的图片\\学习强国电台.png'
    # login = '.\\使用的图片\\学习强国登陆.png'
    # flag = 1
    # while flag == 1:
    #     if pag.locateOnScreen(login):
    #         denglu()
    #         continue
    #     elif pag.locateOnScreen(diantai):
    #         move_and_click(diantai)
    #         flag = 0
    #     else:
    #         print('正在识别是否需要登录…')
    #         continue
    # tingwenhua = '.\\使用的图片\\学习强国听文化.png'
    # flag = 1
    # while flag == 1:
    #     try:
    #         move_and_click(tingwenhua)
    #         flag = 0
    #     except:
    #         continue
    # tingyinyue = '.\\使用的图片\\听音乐.png'
    # tingyinyue2 = '.\\使用的图片\\听音乐2.png'
    # flag = 1
    # while flag == 1:
    #     if pag.locateOnScreen(tingyinyue):
    #         move_and_click(tingyinyue)
    #         flag = 0
    #     elif pag.locateOnScreen(tingyinyue2):
    #         move_and_click(tingyinyue2)
    #         flag = 0
    #     else:
    #         print('正在查找听音乐……')
    #         continue
    # time.sleep(2)
    # pag.moveRel(0, 750, duration=0.25)
    # pag.click()
    # time.sleep(2)
    # bofangquanbu = '.\\使用的图片\\全部播放.png'
    # flag = 1
    # while flag == 1:
    #     try:
    #         move_and_click(bofangquanbu)
    #         flag = 0
    #     except:
    #         continue
    # time.sleep(10)
    # pag.moveRel(69,660,duration=0.5)
    # pag.click()
    # time.sleep(10)
    # pag.click()
    # news =  '.\\使用的图片\\学习强国新闻.png'
    # while not pag.locateOnScreen(news):
    #     print('正在查找学习新闻界面…')
    # move_and_click(news)
    # time.sleep(2)
    # guizhou = '.\\使用的图片\\贵州频道.png'
    # while not pag.locateOnScreen(guizhou):
    #     print('正在等待界面显示…')
    # move_and_click(guizhou)
    # guizhoupt = '.\\使用的图片\\贵州学习平台.png'
    # while not pag.locateOnScreen(guizhoupt):
    #     print('正在等待界面显示…')
    # move_and_click(guizhoupt)
    # time.sleep(2)
    # pag.moveRel(480,700,duration=1)
    # time.sleep(2)
    # pag.click()
    # time.sleep(2)
    # pag.moveRel(-382,-602,duration=0.45)
    # pag.click()
    while True:
        print('正在等待界面显示…')
        n=pag.locateAllOnScreen('.\\使用的图片\\贵州频道文章显示完毕.png')
        if  pag.locateAllOnScreen('.\\使用的图片\\贵州频道文章显示完毕.png'):
            pag.moveRel(384, 594, duration=0.45)
            time.sleep(2)
            # pag.click()
            break
        else:
            pass







    # pag.moveRel(0,-165,duration=2)
    # time.sleep(1)
    # pag.click()
    # time.sleep(3)
    # xianshi = '.\\使用的图片\\推荐文章显示标识.png'
    # while not pag.locateOnScreen(xianshi):
    #     print('正在等待文章显示…')
    # shoucang = '.\\使用的图片\\文章收藏标识.png'
    # while not pag.locateOnScreen(shoucang):
    #     print('正在查找收藏按钮…')
    # move_and_click(shoucang)
    # time.sleep(3)
    # pag.moveRel(-412,-2,duration=0.45)
    # pag.click()
    # time.sleep(3)
    # pag.click()
    # tmplist=['习近平新时代中国特色社会主义思想必将取得伟大的胜利',
    #          '沿着正确的道路，中华民族必将迎来伟大的复兴',
    #          '新时代，新思想，中国特色社会主义五位一体建设必将引领中华民'
    #          '族的复兴',
    #          '新时代，新思想，中国特色社会主义的道路必将引领人类的发展潮流']
    # i = random.randint(0,len(tmplist)-1)
    # j = '！'*random.randint(1,4)
    # pinglun = tmplist[i]+j
    # pyperclip.copy(pinglun)
    # pag.hotkey('ctrl','V')
    # pag.moveRel(453,-47,duration=0.45)
    # pag.click()
    # pag.moveRel(54,58,duration=0.45)
    # pag.click()


    # flag = 1
    # while flag == 1:
    #     try:
    #         x, y = pag.center(pag.locateOnScreen(guizhoupt))
    #         pag.moveTo(x,y,duration=0.25)
    #         flag = 0
    #     except:
    #         continue
    # pag.moveRel(30,100,duration=0.25)
    # pag.click()
    # time.sleep(3)
    # mousescroll()
    # fenxiang = '.\\使用的图片\\学习强国分享.png'
    # fen_xiang_duan_xin = '.\\使用的图片\\分享到短信.png'
    # fen_xiang_ping_tai = '.\\使用的图片\\分享到平台.png'
    # move_and_click(fenxiang)
    # time.sleep(5)
    # while not pag.locateOnScreen(fen_xiang_ping_tai):
    #     print('正在打开分享界面…')
    #     pag.click()
    #     time.sleep(5)
    # flag = 1
    # while flag == 1:
    #     try:
    #         move_and_click(fen_xiang_duan_xin)
    #         flag = 0
    #     except:
    #         continue
    # time.sleep(1)
    # flag = 1
    # while flag == 1:
    #     try:
    #         move_and_click(fenxiang)
    #         flag = 0
    #     except:
    #         continue
    # flag = 1
    # while flag == 1:
    #     try:
    #         move_and_click(fen_xiang_ping_tai)
    #         flag = 0
    #     except:
    #         continue
    # fenxiangfanhuidingwei = '.\\使用的图片\\分享返回定位标识.png'
    # flag = 1
    # while flag == 1:
    #     try:
    #         move_and_click(fenxiangfanhuidingwei)
    #         flag = 0
    #     except:
    #         continue
    # pag.moveRel(-232,0,duration=0.25)
    # pag.click()
    # time.sleep(5)
    # pag.click()




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
    n='.\\使用的图片\\蓝叠APP.png'
    n1='.\\使用的图片\\蓝叠app是否启动.png'
    if pag.locateOnScreen(n):
        while not pag.locateOnScreen(n1):
            move_and_click(n)
            time.sleep(1.5)
            pag.doubleClick()
            time.sleep(5)
        flag = 1
        while flag == 1:
            try:
                openxxqg()
                flag = 0
            except:
                print('正在查找学习强国APP…')
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
    n='.\\使用的图片\\学习强国APP.png'
    move_and_click(n)

#定义一个函数，操作学习强国的登陆
def denglu():
    n= '.\\使用的图片\\学习强国登陆.png'
    flag =1
    while flag==1:
        try:
            move_and_click(n)
            pag.write('1986122',0.8)
            time.sleep(0.25)
            pag.press('enter')
            flag=0
        except:
            print('查找登陆界面中…')
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


# movetocenter()

main()


