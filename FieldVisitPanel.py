import wx
import os
import sys
from DropdownTime import *


class FieldVisitPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        super(FieldVisitPanel, self).__init__(*args, **kwargs)

        self.backgroundColor = (240, 240, 240, 255)
        self.dir = os.path.dirname(os.path.realpath(sys.argv[0]))
        self.margin = (20, 20)
        self.rowSize = (150, 24)
        
        self.rowSizer = []
        self.removeList = []
        self.workEntry = []
        self.accessEntry = []
        self.activityEntry = []
        self.riskEntry = []

        self.location = []

        

        self.InitUI()

    def InitUI(self):
        self.layout = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.layout)
        self.SetBackgroundColour(self.backgroundColor)

        font = wx.Font(9, wx.SWISS, wx.NORMAL, wx.NORMAL)
        entryFont = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        self.SetFont(font)

        generalSizer = wx.BoxSizer(wx.HORIZONTAL)

        categorySizer = wx.BoxSizer(wx.VERTICAL)
        categoryPanel = wx.Panel(self, style=wx.SIMPLE_BORDER)
        categoryPanel.SetBackgroundColour(wx.WHITE)
        categoryPanel.SetSizer(categorySizer)

        categoryLabel = wx.StaticText(categoryPanel, label="       Field Visit", size=(115, -1))
        categorySizer.Add((-1, 5))
        categorySizer.Add(categoryLabel)
        categorySizer.Add((-1, 5))

        self.removeButton = wx.Button(self, label="-", size=(28, 28))

        generalSizer.Add(categoryPanel)
        generalSizer.Add(self.removeButton)

        # Start time
        startSizer = wx.BoxSizer(wx.VERTICAL)
        startPanel = wx.Panel(self, style=wx.SIMPLE_BORDER)
        startPanel.SetSizer(startSizer)

        startHeader = wx.StaticText(startPanel, label="  START TIME")
        startEntrySizer = wx.BoxSizer(wx.HORIZONTAL)
        startEntry = DropdownTime(startPanel, size=(160, -1))
        startEntry.SetFont(entryFont)
        startEntrySizer.Add((5, -1))
        startEntrySizer.Add(startEntry)
        startEntrySizer.Add((5, -1))

        startSizer.Add(startHeader)
        startSizer.Add((-1, 5))
        startSizer.Add(startEntrySizer)
        startSizer.Add((-1, 10))
        
        # Content
        contentSizer = wx.BoxSizer(wx.VERTICAL)
        self.contentPanel = wx.Panel(self, style=wx.SIMPLE_BORDER)
        self.contentPanel.SetSizer(contentSizer)
        self.contentPanel.SetFont(entryFont)
        
        labelSizer = wx.BoxSizer(wx.HORIZONTAL)
        
        buttonPanel = wx.Panel(self.contentPanel, style=wx.SIMPLE_BORDER, size=(24, 24))
        
        workSizer = wx.BoxSizer(wx.HORIZONTAL)
        workPanel = wx.Panel(self.contentPanel, style=wx.SIMPLE_BORDER, size=self.rowSize)
        workPanel.SetSizer(workSizer)
        workHeader = wx.StaticText(workPanel, label=" Work Location")
        workSizer.Add(workHeader)

        accessSizer = wx.BoxSizer(wx.HORIZONTAL)
        accessPanel = wx.Panel(self.contentPanel, style=wx.SIMPLE_BORDER, size=self.rowSize)
        accessPanel.SetSizer(accessSizer)
        accessHeader = wx.StaticText(accessPanel, label=" Access Details")
        accessSizer.Add(accessHeader)

        activitySizer = wx.BoxSizer(wx.HORIZONTAL)
        activityPanel = wx.Panel(self.contentPanel, style=wx.SIMPLE_BORDER, size=self.rowSize)
        activityPanel.SetSizer(activitySizer)
        activityHeader = wx.StaticText(activityPanel, label=" Field Activities")
        activitySizer.Add(activityHeader)

        riskSizer = wx.BoxSizer(wx.HORIZONTAL)
        riskPanel = wx.Panel(self.contentPanel, style=wx.SIMPLE_BORDER, size=self.rowSize)
        riskPanel.SetSizer(riskSizer)
        riskHeader = wx.StaticText(riskPanel, label=" Risk")
        riskSizer.Add(riskHeader)
        
        labelSizer.Add(buttonPanel)
        labelSizer.Add(workPanel)
        labelSizer.Add(accessPanel)
        labelSizer.Add(activityPanel)
        labelSizer.Add(riskPanel)
        
        self.tableSizer = wx.BoxSizer(wx.VERTICAL)
        
        addSizer = wx.BoxSizer(wx.HORIZONTAL)
        addButton = wx.Button(self.contentPanel, label="+", size=(24, 24))
        addButton.Bind(wx.EVT_BUTTON, self.addRow)
        addSizer.Add(addButton)
        
        contentSizer.Add(labelSizer)
        contentSizer.Add(self.tableSizer)
        contentSizer.Add(addSizer)

        # End time
        endSizer = wx.BoxSizer(wx.VERTICAL)
        endPanel = wx.Panel(self, style=wx.SIMPLE_BORDER)
        endPanel.SetSizer(endSizer)

        endHeader = wx.StaticText(endPanel, label="  END TIME")
        endEntrySizer = wx.BoxSizer(wx.HORIZONTAL)
        endEntry = DropdownTime(endPanel, size=(160, -1))
        endEntry.SetFont(entryFont)
        endEntrySizer.Add((10, -1))
        endEntrySizer.Add(endEntry)
        endEntrySizer.Add((10, -1))

        endSizer.Add(endHeader)
        endSizer.Add((-1, 5))
        endSizer.Add(endEntrySizer)
        endSizer.Add((-1, 10))

        self.layout.Add(generalSizer)
        self.layout.Add((-1, 10))
        self.layout.Add(startPanel)
        self.layout.Add((-1, 10))
        self.layout.Add(self.contentPanel)
        self.layout.Add((-1, 10))
        self.layout.Add(endPanel)
        
        self.addRow(None)
        
        self.layout.Add(self.margin)

        self.Refresh()

    def addRow(self, event):
        self.rowSizer.append(wx.BoxSizer(wx.HORIZONTAL))
        self.removeList.append(wx.Button(self.contentPanel, label="-", size=(24, 24)))
        self.removeList[-1].Bind(wx.EVT_BUTTON, self.removeRow)
        self.workEntry.append(wx.ComboBox(self.contentPanel, size=self.rowSize))
        self.accessEntry.append(wx.ComboBox(self.contentPanel, size=self.rowSize))
        self.activityEntry.append(wx.ComboBox(self.contentPanel, size=self.rowSize))
        self.riskEntry.append(wx.ComboBox(self.contentPanel, size=self.rowSize))
        
        self.rowSizer[-1].Add(self.removeList[-1])
        self.rowSizer[-1].Add(self.workEntry[-1])
        self.rowSizer[-1].Add(self.accessEntry[-1])
        self.rowSizer[-1].Add(self.activityEntry[-1])
        self.rowSizer[-1].Add(self.riskEntry[-1])
        
        self.tableSizer.Add(self.rowSizer[-1])
        self.GetParent().Layout()
        
    def removeRow(self, event):
        id = self.removeList.index(event.GetEventObject())
        
        self.removeList[id].Destroy()
        self.workEntry[id].Destroy()
        self.accessEntry[id].Destroy()
        self.activityEntry[id].Destroy()
        self.riskEntry[id].Destroy()

        del self.rowSizer[id]
        del self.removeList[id]
        del self.workEntry[id]
        del self.accessEntry[id]
        del self.activityEntry[id]
        del self.riskEntry[id]

        self.GetParent().Layout()
        
def main():
    app = wx.App()
    frame = wx.Frame(None, size=(1200, 650))
    FieldVisitPanel("", "debug", frame)
    frame.Centre()
    frame.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
