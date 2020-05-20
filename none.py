import tkinter
import pyautogui as pag
import win32api,win32gui
import win32con
import pyperclip
import time

# root = tkinter.Tk()
# label = tkinter.Label(root,text='获取鼠标移动值')
# label.pack()
#
# root.mainloop()


hw = win32gui.FindWindow('BS2CHINAUI','BlueStacks App Player')
# win32gui.ShowWindow(hw,win32con.SW_SHOWNORMAL)
# print(win32gui.IsIconic(hw))
print(win32gui.GetWindowRect(hw))
tmp = win32gui.GetWindowRect(hw)
print(pag.center(tmp))
# win32gui.SetForegroundWindow(hw)
# x, y = pag.center(tmp)
# pag.moveTo(x,y,duration=1)

# hw1 = win32gui.FindWindow('Notepad','新建文本文档.txt - 记事本')
# print(win32gui.GetWindowRect(hw1))
# win32gui.SetForegroundWindow(hw1)
# # time.sleep(1)
# # n=['什么是人？','什么是神？','什么是完美？']
# # for i in n:
# #     pyperclip.copy(i)
# #     pag.hotkey('ctrl','v')
# #     pag.press('enter')
# tmp = win32gui.GetWindowRect(hw1)
# x, y = pag.center(tmp)
def woyaodayin():
    print('hello world!')

def newcenter(str):
    '''newcenter函数用来计算并返回一个矩形坐标的中心坐标值'''
    x0,y0,x1,y1=str
    x = (x1-x0)/2+x0
    y = (y1-y0)/2+y0
    return x, y


# woyaodayin()
# x,y = newcenter(tmp)
#
# # print(x0,y0,x1,y1)
# # pag.moveTo(x,y,duration=1)
# pag.moveTo(x,y,duration=1)




