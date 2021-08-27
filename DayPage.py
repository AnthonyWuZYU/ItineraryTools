import wx
import os
import sys
import wx.adv as adv
import wx.lib.scrolledpanel as scrolled

from AccommodationPanel import *
from FieldVisitPanel import *
from TravelPanel import *

class DayPage(scrolled.ScrolledPanel):
    def __init__(self, mode, ver, *args, **kwargs):
        super(DayPage, self).__init__(*args, **kwargs)

        self.backgroundColor = (240, 240, 240, 255)
        self.dir = os.path.dirname(os.path.realpath(sys.argv[0]))
        self.margin = (20, 20)
        self.category = ["", "Field Visit", "Travel", "Accommodation"]
        self.fieldList = []
        self.travelList = []
        self.accommodationList = []
        
        self.InitUI()

    def InitUI(self):
        self.layout = wx.BoxSizer(wx.HORIZONTAL)
        self.SetSizer(self.layout)
        self.SetBackgroundColour(self.backgroundColor)
        
        mainSizer = wx.BoxSizer(wx.VERTICAL)

        font = wx.Font(9, wx.SWISS, wx.NORMAL, wx.NORMAL)
        entryFont = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        self.SetFont(font)
        
        generalSizer = wx.BoxSizer(wx.HORIZONTAL)
        
        # date
        dateSizer = wx.BoxSizer(wx.VERTICAL)
        datePanel = wx.Panel(self, style=wx.SIMPLE_BORDER)
        datePanel.SetSizer(dateSizer)
        
        dateHeader = wx.StaticText(datePanel, label="  DATE(yyyy/mm/dd)")
        dateEntrySizer = wx.BoxSizer(wx.HORIZONTAL)
        dateEntry = adv.DatePickerCtrl(datePanel, style=wx.adv.DP_DROPDOWN)
        dateEntry.SetFont(entryFont)
        dateEntrySizer.Add((10, -1))
        dateEntrySizer.Add(dateEntry)
        dateEntrySizer.Add((10, -1))
        
        dateSizer.Add(dateHeader)
        dateSizer.Add((-1, 5))
        dateSizer.Add(dateEntrySizer)
        dateSizer.Add((-1, 5))

        # daily comment section
        commentSizer = wx.BoxSizer(wx.VERTICAL)
        commentPanel = wx.Panel(self, style=wx.SIMPLE_BORDER)
        commentPanel.SetSizer(commentSizer)

        commentHeader = wx.StaticText(commentPanel, label="  DAILY COMMENTS")
        commentEntrySizer = wx.BoxSizer(wx.HORIZONTAL)
        commentEntry = wx.TextCtrl(commentPanel, size=(600, -1))
        commentEntrySizer.Add((10, -1))
        commentEntrySizer.Add(commentEntry)
        commentEntrySizer.Add((10, -1))

        commentSizer.Add(commentHeader)
        commentSizer.Add((-1, 5))
        commentSizer.Add(commentEntrySizer)
        commentSizer.Add((-1, 5))
        
        generalSizer.Add(datePanel)
        generalSizer.Add(self.margin)
        generalSizer.Add(commentPanel)
        
        # all the form of categories
        self.formGroupSizer = wx.BoxSizer(wx.VERTICAL)

        # Select category

        categorySizer = wx.BoxSizer(wx.VERTICAL)
        categoryPanel = wx.Panel(self, style=wx.SIMPLE_BORDER)
        categoryPanel.SetSizer(categorySizer)

        categoryEntrySizer = wx.BoxSizer(wx.HORIZONTAL)
        categoryEntry = wx.ComboBox(categoryPanel, style=wx.TE_READONLY, size=(150, -1))
        categoryEntry.SetItems(self.category)
        categoryEntry.Bind(wx.EVT_TEXT, self.addForm)
        categoryEntrySizer.Add((10, -1))
        categoryEntrySizer.Add(categoryEntry)
        categoryEntrySizer.Add((10, -1))

        categorySizer.Add((-1, 5))
        categorySizer.Add(categoryEntrySizer)
        categorySizer.Add((-1, 5))
        
        mainSizer.Add(self.margin)
        mainSizer.Add(generalSizer)
        mainSizer.Add(self.margin)
        mainSizer.Add(self.formGroupSizer)
        mainSizer.Add(categoryPanel)
        
        self.layout.Add(self.margin)
        self.layout.Add(mainSizer)
        
        self.SetupScrolling()
        self.SetDoubleBuffered(True)
        self.Refresh()
        
    def addForm(self, event):
        category = event.GetEventObject().GetValue()
        
        if category == "Field Visit":
            self.fieldList.append(FieldVisitPanel(self))
            self.fieldList[-1].removeButton.Bind(wx.EVT_BUTTON, self.removeFieldVisit)
            self.formGroupSizer.Add(self.fieldList[-1])
        elif category == "Travel":
            self.fieldList.append(TravelPanel(self))
            self.fieldList[-1].removeButton.Bind(wx.EVT_BUTTON, self.removeFieldVisit)
            self.formGroupSizer.Add(self.fieldList[-1])
        elif category == "Accommodation":
            self.accommodationList.append(AccommodationPanel(self))
            self.accommodationList[-1].removeButton.Bind(wx.EVT_BUTTON, self.removeAccommodation)
            self.formGroupSizer.Add(self.accommodationList[-1])
        else:
            return

        event.GetEventObject().SetValue("")
        
        self.layout.Layout()
        self.GetParent().Layout()
        self.Update()
    
    def removeAccommodation(self, event):
        id = self.accommodationList.index(event.GetEventObject().GetParent())
        event.GetEventObject().GetParent().Destroy()
        del self.accommodationList[id]
        
        self.Layout()

    def removeFieldVisit(self, event):
        id = self.fieldList.index(event.GetEventObject().GetParent())
        event.GetEventObject().GetParent().Destroy()
        del self.fieldList[id]

        self.Layout()
        
def main():
    app = wx.App()
    frame = wx.Frame(None, size=(1200, 650))
    DayPage("", "debug", frame)
    frame.Centre()
    frame.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
