import pyautogui as pag


def newcenter(str):
    '''newcenter函数用来计算并返回一个矩形坐标的中心坐标值'''
    x0,y0,x1,y1=str
    x = (x1-x0)/2+x0
    y = (y1-y0)/2+y0
    return x, y

def movetocenter(x,y):
    '''movetocenter函数用来移动到窗口的中心位置'''



if __name__ == '__main__':
    n=(1,2,3,4)
    x,y = newcenter(n)
    print(x,y)



