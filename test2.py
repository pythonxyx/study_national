import win32api
import os

# win32api.ShellExecute(0,'open','F:\\Program Files (x86)\\BluestacksCN\\BlueStacksGP.exe','','',1)
os.chdir('F:\\Program Files (x86)\\BluestacksCN')
os.system('BlueStacksGP.exe -p cn.xuexi.android')