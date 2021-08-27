import sys
import wx
from LoginPage import *
from mainPage import *
from ItineraryPage import *

mode = "Debug"
ITINERARY_VERSION = "v1.0"

class ItineraryTool:
    def __init__(self):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        
        self.headerTitle = "Itinerary Tool"
        self.logoutConfirm = "Are you sure about logging out?"
        self.createItineraryConfirm = "Create an New Itinerary Form."
        self.createToMainConfirm = "Go back to main page."
        
        
        self.loginSize = (400, 450)
        self.mainPageSize = (400, 450)
        self.itinerarySize = (1200, 650)
        
        self.InitUI()

    def InitUI(self):
        app = wx.App()
        
        # Login Window
        self.loginPage = LoginPage(mode, ITINERARY_VERSION, None, title=self.headerTitle, size=self.loginSize)
        self.loginPage.Centre()
        self.loginPage.Show()
        self.loginPage.loginButton.Bind(wx.EVT_BUTTON, self.login)

        app.MainLoop()
        
    def login(self, event):
        username = self.loginPage.returnUsername()
        password = self.loginPage.returnPassword()
        
        # verification
    
    
        # Destroy login page | show itinerary page
        self.loginPage.Destroy()
        self.mainPage = mainPage(mode, ITINERARY_VERSION, username, password, None, title=self.headerTitle, size=self.mainPageSize)
        self.mainPage.Centre()
        self.mainPage.Show()
        self.mainPage.logoutLink.Bind(wx.EVT_BUTTON, self.logout)
        self.mainPage.createItinerary.Bind(wx.EVT_BUTTON, self.createItinerary)
        
    def logout(self, event):
        # Confirmation of logging out
        dlg = wx.MessageDialog(self.mainPage, self.logoutConfirm, 'Logging out', wx.YES_NO)
        res = dlg.ShowModal()
        if res == wx.ID_YES:
            # Destroy itinerary page | show login page
            self.mainPage.Destroy()
            self.loginPage = LoginPage(mode, ITINERARY_VERSION, None, title=self.headerTitle, size=self.loginSize)
            self.loginPage.Centre()
            self.loginPage.Show()
            self.loginPage.loginButton.Bind(wx.EVT_BUTTON, self.login)
            
    def createItinerary(self, event):
        dlg = wx.MessageDialog(self.mainPage, self.createItineraryConfirm, 'New Itinerary From', wx.YES_NO)
        res = dlg.ShowModal()
        if res == wx.ID_YES:
            username = self.mainPage.username
            password = self.mainPage.password
            # Destroy itinerary page | show login page
            self.mainPage.Destroy()
            self.itineraryPage = itineraryPage(mode, ITINERARY_VERSION, username, password, None, title=self.headerTitle, size= self.itinerarySize)
            self.itineraryPage.Centre()
            self.itineraryPage.Show()
            self.itineraryPage.fieldPage.backButton.Bind(wx.EVT_BUTTON, self.createBackToMain)

    def createBackToMain(self, event):
        dlg = wx.MessageDialog(self.itineraryPage, self.createToMainConfirm, 'Back to Main Page', wx.YES_NO)
        res = dlg.ShowModal()
        if res == wx.ID_YES:
            username = self.mainPage.username
            password = self.mainPage.password
            # Destroy itinerary page | show login page
            self.itineraryPage.Destroy()
            self.mainPage = mainPage(mode, ITINERARY_VERSION, username, password, None, title=self.headerTitle, size= self.mainPageSize)
            self.mainPage.Centre()
            self.mainPage.Show()
            self.mainPage.logoutLink.Bind(wx.EVT_BUTTON, self.logout)
            self.mainPage.createItinerary.Bind(wx.EVT_BUTTON, self.createItinerary)
        

def main():
    gui = ItineraryTool()


if __name__=='__main__':
    main()