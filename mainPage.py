import wx
import os
import sys


class mainPage(wx.Frame):
    def __init__(self, mode, ver, username, password, *args, **kwargs):
        super(mainPage, self).__init__(*args, **kwargs)

        self.username = username
        self.password = password
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

        self.itineraryPanel = wx.Panel(self)
        self.itineraryPanel.SetBackgroundColour(wx.WHITE)

        headerFont = wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL)
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        
        # Log out option
        logoutSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.logoutLink = wx.Button(self.itineraryPanel, label="Log Out", size=(53, -1), style=wx.NO_BORDER)
        self.logoutLink.SetBackgroundColour(wx.WHITE)
        self.logoutLink.SetForegroundColour(wx.RED)
        self.logoutLink.SetFont(font)
        logoutSizer.Add((-1, -1), wx.EXPAND)
        logoutSizer.Add(self.logoutLink)
        
        
        # Logo
        logoSizer = wx.BoxSizer(wx.HORIZONTAL)
        logoSize = 150
        logo = wx.Image(self.logo_path, wx.BITMAP_TYPE_ANY).Scale(logoSize, logoSize)
        bitLogo = wx.StaticBitmap(self.itineraryPanel, -1, logo.ConvertToBitmap())
        logoSizer.Add(bitLogo, wx.CENTRE)
        
        itinerarySizer = wx.BoxSizer(wx.VERTICAL)
        self.itineraryPanel.SetSizer(itinerarySizer)

        
        # User Information
        infoSizer = wx.BoxSizer(wx.HORIZONTAL)
        userLabel = wx.StaticText(self.itineraryPanel, label = " User: " + self.username)
        userLabel.SetFont(headerFont)
        
        
        
        infoSizer.Add(userLabel)
        infoSizer.Add((-1, -1), wx.EXPAND)
        
        roleSizer = wx.BoxSizer(wx.HORIZONTAL)
        roleLabel = wx.StaticText(self.itineraryPanel, label="Role: Dev")
        roleLabel.SetFont(headerFont)
        
        roleSizer.Add((4, -1))
        roleSizer.Add(roleLabel)
        
        
        optionSizer = wx.BoxSizer(wx.VERTICAL)
        self.createItinerary = wx.Button(self.itineraryPanel, label = "Create New Itinerary", size = (-1, 56))
        self.createItinerary.SetFont(headerFont)
        self.editItinerary = wx.Button(self.itineraryPanel, label="Edit/View Itineraries", size = (-1, 56))
        self.editItinerary.SetFont(headerFont)
        self.editDatabase = wx.Button(self.itineraryPanel, label="Edit Database", size = (-1, 56))
        self.editDatabase.SetFont(headerFont)
        
        optionSizer.Add(self.createItinerary, 1, wx.EXPAND)
        optionSizer.Add(self.editItinerary, 1, wx.EXPAND)
        optionSizer.Add(self.editDatabase, 1, wx.EXPAND)

        itinerarySizer.Add(logoutSizer, 0, wx.EXPAND)
        itinerarySizer.Add(logoSizer, 0, wx.EXPAND)
        itinerarySizer.Add((-1, 9))
        itinerarySizer.Add(infoSizer, 0, wx.EXPAND)
        itinerarySizer.Add((-1, 10))
        itinerarySizer.Add(roleSizer, 0, wx.EXPAND)
        itinerarySizer.Add((-1, 10))
        itinerarySizer.Add(optionSizer, 0, wx.EXPAND)
        
        mainSizer.Add(self.itineraryPanel, 1, wx.EXPAND)
        
        


def main():
    app = wx.App()

    page = mainPage("", "", "Test", "", None, size = (400, 255))
    page.Centre()
    page.Show()
    app.MainLoop()


if __name__=='__main__':
    main()
