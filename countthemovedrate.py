import pyautogui as pag
import os
import pyperclip

flag = 1
while flag == 1:
    print('---------鼠标移动值测量程序---------')
    print('')
    input('回车键获得鼠标的当前位置坐标…')
    x,y = pag.position()
    print('移动前鼠标的位置是%d，%d'%(x,y))
    input('回车获得移动后鼠标的位置坐标…')
    x1,y1 = pag.position()
    print('移动后鼠标的位置是%d，%d'%(x1,y1))
    x0 = x1-x
    y0 = y1-y
    print('\n\n鼠标移动的相对量为%d，%d'%(x0,y0))
    print('')
    pyperclip.copy(str(x0)+','+str(y0))
    print('已经复制到剪切板！')
    print('')
    n = input('''请选择接下来的操作：
    1--将移动值保存到文件,鼠标返回原始位置
    2--返回原始位置继续查询
    3--不保存继续新的查询
    直接回车键退出程序！''')
    if n == '1' :
        if not os.path.exists('移动值保存文件夹'):
            os.makedirs('移动值保存文件夹')
        name = input('请输入需要保存的文件或追加的名字：')
        name1 = input('请输入移动量值的名称：')
        with open('.\\'+'移动值保存文件夹'+'\\'+name+'.txt','a+') as file:
            file.write('【%s】 位置的相对移动量为（%d，%d）\n'%(name1,x0,y0))
        print('保存成功！是否需要继续查询？')
        n1 = input('1-继续查询。 直接回车退出程序！')
        if n1 == '1':
            pass
        else:
            flag = 0
    elif n == '2':
        pag.moveTo(x,y,duration=0.45)
    elif n == '3':
        pass
    else:
        break