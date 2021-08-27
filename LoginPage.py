import wx
import os
import sys


class LoginPage(wx.Frame):
    def __init__(self, mode, ver, *args, **kwargs):
        super(LoginPage, self).__init__(*args, **kwargs)

        self.iconName = "icon_transparent.ico"
        self.logoName = "icon_transparent.png"
        
        self.dir = os.path.dirname(os.path.realpath(sys.argv[0]))
        self.icon_path = self.iconName
        self.logo_path = self.logoName
        
        if hasattr(sys, '_MEIPASS'):
            self.icon_path = os.path.join(sys._MEIPASS, self.icon_path)
            self.logo_path = os.path.join(sys._MEIPASS, self.logo_path)
        else:
            self.icon_path = os.path.join(self.dir, self.icon_path)
            self.logo_path = os.path.join(self.dir, self.logo_path)
        
        if os.path.exists(self.icon_path):
            png = wx.Image(self.icon_path, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
            self.icon = wx.Icon(png)
            self.SetIcon(self.icon)
        
        self.InitUI()
        
    def InitUI(self):
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(mainSizer)
        
        self.loginPanel = wx.Panel(self)
        self.loginPanel.SetBackgroundColour(wx.WHITE)
        
        loginSizer = wx.BoxSizer(wx.VERTICAL)
        self.loginPanel.SetSizer(loginSizer)
    
        headerFont = wx.Font(16, wx.SWISS, wx.NORMAL, wx.NORMAL)
        font = wx.Font(13, wx.SWISS, wx.NORMAL, wx.NORMAL)
        entryFont = wx.Font(13, wx.SWISS, wx.NORMAL, wx.LIGHT)
        
        # Logo
        logoSizer = wx.BoxSizer(wx.HORIZONTAL)
        logoSize = 150
        logo = wx.Image(self.logo_path, wx.BITMAP_TYPE_ANY).Scale(logoSize, logoSize)
        bitLogo = wx.StaticBitmap(self.loginPanel, -1, logo.ConvertToBitmap())
        logoSizer.Add(bitLogo, wx.CENTRE)
        
        # Header
        headerSizer = wx.BoxSizer(wx.HORIZONTAL)
        headerLabel = wx.StaticText(self.loginPanel, label="Login to your account")
        headerLabel.SetFont(headerFont)
        headerSizer.Add((-1,-1), 1, wx.EXPAND)
        headerSizer.Add(headerLabel)
        headerSizer.Add((-1, -1), 1, wx.EXPAND)
        
        # User Entry
        userSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.userEntry = wx.TextCtrl(self.loginPanel, size=(250, 34))
        self.userEntry.SetHint("Username")
        self.userEntry.SetFont(entryFont)
        userSizer.Add((-1, -1), 1, wx.EXPAND)
        userSizer.Add(self.userEntry)
        userSizer.Add((-1, -1), 1, wx.EXPAND)
        
        # Password Entry
        passwordSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.passwordEntry = wx.TextCtrl(self.loginPanel, size=(250, 34), style=wx.TE_PASSWORD)
        self.passwordEntry.SetHint("Password")
        self.passwordEntry.SetFont(entryFont)
        passwordSizer.Add((-1, -1), 1, wx.EXPAND)
        passwordSizer.Add(self.passwordEntry)
        passwordSizer.Add((-1, -1), 1, wx.EXPAND)
        
        # Login Button
        buttonSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.loginButton = wx.Button(self.loginPanel, size=(250, 34), label="Log in", style=wx.NO_BORDER)
        self.loginButton.SetBackgroundColour(wx.Colour("#00cc44"))
        self.loginButton.SetForegroundColour(wx.WHITE)
        self.loginButton.SetFont(font)
        buttonSizer.Add((-1, -1), 1, wx.EXPAND)
        buttonSizer.Add(self.loginButton)
        buttonSizer.Add((-1, -1), 1, wx.EXPAND)

        loginSizer.Add((-1, 20))
        loginSizer.Add(logoSizer, 0, wx.EXPAND)
        loginSizer.Add((-1, 10))
        loginSizer.Add(headerSizer, 0, wx.EXPAND)
        loginSizer.Add((-1, 20))
        loginSizer.Add(userSizer, 0, wx.EXPAND)
        loginSizer.Add(passwordSizer, 0, wx.EXPAND)
        loginSizer.Add((-1, 20))
        loginSizer.Add(buttonSizer, 0, wx.EXPAND)
        
        mainSizer.Add(self.loginPanel, 1, wx.EXPAND)
        
    def returnUsername(self):
        return self.userEntry.GetValue()
    
    def returnPassword(self):
        return self.passwordEntry.GetValue()
        
def main():
    app = wx.App()

    page = LoginPage("", "", None)

    page.Show()
    app.MainLoop()


if __name__=='__main__':
    main()
        