import wx

from com.jcl.petstore.ui.login_frame import LoginFrame

class App(wx.App):
    def OnInit(self):
        #创建窗口对象
        frame = LoginFrame()
        frame.Show()
        return True

if __name__ == '__main__':
    app = App()
    app.MainLoop()