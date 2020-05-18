import pyautogui as pag


#测试鼠标位置
def testmouse(x,y):
    pag.moveRel(x,y,duration=1)
    n = input('请输入下步操作：1-继续测试，2-结束测试，回车键鼠标回原始位置！')
    if n == '1':
        pass
    else:
        pag.moveRel(-x,-y,duration=1)

while True:
    x = int(input("请输入x的值："))
    y = int(input('请输入y的值：'))
    print('你输入的x值是%d，y值是%d'%(x,y))
    testmouse(x,y)