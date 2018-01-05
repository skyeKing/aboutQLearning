# coding:utf-8
'''
1）根据标题获取窗口句柄
2）将窗口置于最前端
3）根据窗口句柄获取窗口矩阵rect
4）截图窗口区域
'''
#print sys.getdefaultencoding()
import win32api,win32gui,os,time
import PIL.ImageGrab as ImageGrab
WindowTitleText = u'登录'
saveImgPath = 'd:/Desktop/saveImgPath'
hwnd = win32gui.FindWindow(None,WindowTitleText)
win32gui.EnableWindow(hwnd,True)
win32gui.SetForegroundWindow(hwnd)
bbox = left,top,right,bottom = win32gui.GetWindowRect(hwnd)
grabImg = ImageGrab.grab(bbox)
tempImgName = '_'.join(repr(time.time()).split('.'))
tempImgPath = os.path.join(saveImgPath,tempImgName).replace('\\','/')
tempImgFormat = 'png'
grabImg.save('%s.%s'%(tempImgPath,tempImgFormat))
print u'已经保存至',tempImgPath