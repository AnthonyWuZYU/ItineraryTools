import wx
import os
import sys
import wx.lib.scrolledpanel as scrolledpanel

from FieldParty import *
from DayPage import *
from SubmitPanel import *

ID_ADD_DAY = wx.NewId()

class itineraryPage(wx.Frame):
    def __init__(self, mode, ver, username, password, *args, **kwargs):
        super(itineraryPage, self).__init__(*args, **kwargs)

        self.days = 0
        self.daySizer = []
        self.dayForm = []
        self.dayList = []
        self.username = username
        self.password = password
        self.iconName = "icon_transparent.ico"
        self.logoName = "icon_transparent.png"
        self.backgroundColor = (240, 240, 240, 255)

        self.dir = os.path.dirname(os.path.realpath(sys.argv[0]))
        self.icon_path = self.iconName
        self.logo_path = self.logoName

        self.tAddLabel = '&Add Day\tCtrl+A'
        self.tAddDesc = 'Add a new Day'

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

        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()
        toolMenu = wx.Menu()
        tAdd = toolMenu.Append(ID_ADD_DAY, self.tAddLabel, self.tAddDesc)

        self.Bind(wx.EVT_MENU, self.addDay, tAdd)
        
        menuBar.Append(fileMenu, '&File')
        menuBar.Append(toolMenu, '&Tools')
        
        self.SetMenuBar(menuBar)

        self.itineraryPanel = wx.Panel(self)
        self.itineraryPanel.SetBackgroundColour(wx.WHITE)
        itinerarySizer = wx.BoxSizer(wx.VERTICAL)
        
        self.layout = wx.Notebook(self.itineraryPanel, style=wx.NB_TOP)#, agwStyle=fnb.FNB_NO_X_BUTTON|fnb.FNB_NO_NAV_BUTTONS)
        self.layout.SetBackgroundColour(self.backgroundColor)
        
        # Field Page Added
        fieldSizer = wx.BoxSizer(wx.VERTICAL)
        self.fieldForm = wx.Panel(self.layout, style=wx.NO_BORDER)
        self.fieldPage = FieldParty("", "", self.fieldForm)
        fieldSizer.Add(self.fieldPage, 1, wx.EXPAND)
        self.fieldForm.SetSizerAndFit(fieldSizer)

        self.layout.AddPage(self.fieldForm, "FIELD PARTY AND CONTACTS")
        
        itinerarySizer.Add(self.layout, 1, wx.EXPAND)
        self.itineraryPanel.SetSizer(itinerarySizer)

        mainSizer.Add(self.itineraryPanel, 1, wx.EXPAND)
        
        # Add 7 days
        for i in range(7):
            self.addDay(None)
            
        # Submit Page Added
        submitSizer = wx.BoxSizer(wx.VERTICAL)
        self.submitForm = wx.Panel(self.layout, style=wx.NO_BORDER)
        self.submitPage = SubmitPanel("", "", self.submitForm)
        submitSizer.Add(self.submitPage, 1, wx.EXPAND)
        self.submitForm.SetSizerAndFit(submitSizer)

        self.layout.AddPage(self.submitForm, "SUBMIT ")

    def addDay(self, event):
        # Field Page Added
        self.daySizer.append(wx.BoxSizer(wx.VERTICAL))
        self.dayForm.append(wx.Panel(self.layout, style=wx.NO_BORDER))
        self.dayList.append(DayPage("", "", self.dayForm[-1]))
        self.daySizer[-1].Add(self.dayList[-1], 1, wx.EXPAND)
        self.dayForm[-1].SetSizerAndFit(self.daySizer[-1])

        self.layout.InsertPage(len(self.dayForm), self.dayForm[-1], "DAY " + str(len(self.dayList)))

        
        self.Update()
        self.Refresh()
        
def main():
    app = wx.App()

    page = itineraryPage("", "", "Test", "", None, size=(1200, 650))
    page.Centre()
    page.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
